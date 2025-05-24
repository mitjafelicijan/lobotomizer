""" Scrapes warcrafttavern links found in CSV file.  """

import os
import requests
import logging
import pandas as pd

from bs4 import BeautifulSoup
from markdownify import markdownify

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

df = pd.read_csv("warcrafttavern.csv")

for index, row in df.dropna().iterrows():
    response = requests.get(row.url, timeout=20)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("h1")
        content = soup.find("div", id="ftwp-postcontent")

        if title and content:
            logging.info("[%s] -> %s", row["category"], title.text.strip())

            CATEGORY_DIRECTORY = f"../corpus/{row['category']}"
            if not os.path.exists(CATEGORY_DIRECTORY):
                os.makedirs(CATEGORY_DIRECTORY)

            with open(f"{CATEGORY_DIRECTORY}/wct-{row['slug']}.md", "w", encoding="utf-8") as fp:
                fp.write(f"# {title.text.strip()}\n\n")
                fp.write(f"{markdownify(str(content))}")
