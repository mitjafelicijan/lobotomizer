""" Extracts wowhead.com comments. """

import os
import pandas as pd

COMMENTS_DIRECTORY = "../corpus/comments"
if not os.path.exists(COMMENTS_DIRECTORY):
    os.makedirs(COMMENTS_DIRECTORY)

df = pd.read_csv("wowhead_quest_comments.csv")

print(df.head())

print("Column names (header keys):")
for col in df.columns:
    print(col)

for index, row in df.dropna().iterrows():
    with open(f"{COMMENTS_DIRECTORY}/{row['Quest ID']}.md", "w", encoding="utf-8") as fp:
        fp.write(f"# Quest ID: {row['Quest ID']}\n")
        fp.write(f"# Quest Title: {row['Quest Title']}\n")
        fp.write(f"# Quest URL: {row['Quest URL']}\n")
        fp.write(f"# {row['Comments']}")
