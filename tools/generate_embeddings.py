""" Creates embeddings database for double-tapping. """

import os
import sys
import glob
import sqlite3
import argparse
import numpy as np
import logging

from sentence_transformers import SentenceTransformer

CORPUS_DIR = "../corpus"
EMBEDDINGS_MODEL = "all-MiniLM-L6-v2"
DATABASE_PATH = "/tmp/embeddings.db"

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("initializing embedding model")
model = SentenceTransformer(EMBEDDINGS_MODEL)

logging.info("opening database")
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# Create table for documents and embeddings.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY,
        content TEXT,
        embedding BLOB
    )
''')

def index_document(content):
    """ Indexes a document and stores it in a database. """
    embedding = model.encode(content)

    # Convert numpy array to bytes for storage.
    embedding_bytes = embedding.tobytes()
    cursor.execute('INSERT INTO documents (content, embedding) VALUES (?, ?)',
                   (content, embedding_bytes))
    conn.commit()

def search_documents1(query, top_k=5):
    """" Naive search. """
    query_embedding = model.encode(query)
    query_bytes = query_embedding.tobytes()

    cursor.execute('''
        SELECT content 
        FROM documents 
        ORDER BY (
            SELECT SUM((d.embedding - ?) * (d.embedding - ?))
            FROM documents d
            WHERE d.id = documents.id
        ) ASC
        LIMIT ?
    ''', (query_bytes, query_bytes, top_k))

    return cursor.fetchall()


def search_documents(query, top_k=5):
    """" A bit more involved search. """
    query_embedding = model.encode(query)
    query_bytes = query_embedding.tobytes()

    # Get all documents with their embeddings
    cursor.execute('SELECT id, embedding FROM documents')
    rows = cursor.fetchall()

    # Calculate similarities
    results = []
    for row in rows:
        doc_id, emb_bytes = row
        doc_embedding = np.frombuffer(emb_bytes, dtype=np.float32)
        similarity = np.dot(query_embedding, doc_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
        )
        results.append((doc_id, similarity))

    # Sort by similarity and get top K
    results.sort(key=lambda x: x[1], reverse=True)
    top_ids = [x[0] for x in results[:top_k]]

    # Get full document info for top matches
    placeholders = ','.join(['?']*len(top_ids))
    cursor.execute(f'''
        SELECT content FROM documents 
        WHERE id IN ({placeholders})
    ''', top_ids)

    return cursor.fetchall()

def index_corpus():
    """Indexes the whole corpus using glob."""

    # Find all .md files in corpus directory and its subdirectories
    for file_path in glob.glob('../corpus/**/*.md', recursive=True):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                logging.info("indexing '%s'", file_path)
                content = file.read()
                index_document(content)
        except Exception as e:
            logging.error(f"Error processing {file_path}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Tool for creating and querying embeddings database.")
    parser.add_argument("-i", "--index", help="created index database with embeddings", action="store_true")
    parser.add_argument("-s", "--search", help="performs search over the database", type=str, metavar="QUERY")
    parser.add_argument("-n", "--num-results", help="number of results to return (default: 1)", type=int, default=1)
    parser.add_argument("-v", "--verbose", help="verbose messaging", action="store_true")
    args = parser.parse_args()

    if not (args.index or args.search):
        parser.print_help()
        sys.exit(1)

    if args.index:
        index_corpus()

    if args.search:
        logging.info("starting search: %s", args.search)

        results = search_documents(args.search, 1)
        num_tokens = 0
        for i, row in enumerate(results, 1):
            content = row[0]
            num_tokens += len(content.split())

            if args.verbose:
                print(content[:400])

        logging.info(f"num documents: %s", len(results))
        logging.info(f"num tokens: %s", num_tokens)
