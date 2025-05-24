""" Scrapes wowhead links found in CSV file.  """

# If you are running this for the first time do `playwright install` first.

import os
import logging
import pandas as pd

from markdownify import markdownify
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

df = pd.read_csv("wowhead.csv")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for index, row in df.dropna().iterrows():
        try:
            page.goto(row.url)
            page.wait_for_selector("#guide-body", timeout=3000)

            title = page.inner_text("h1")
            content = page.inner_html("#guide-body")

            logging.info("[%s] %s", row["category"], title.strip())

            CATEGORY_DIRECTORY = f"../corpus/{row['category']}"
            if not os.path.exists(CATEGORY_DIRECTORY):
                os.makedirs(CATEGORY_DIRECTORY)

            with open(f"{CATEGORY_DIRECTORY}/wh-{row['slug']}.md", "w", encoding="utf-8") as fp:
                fp.write(f"# {title.strip()}\n\n")
                fp.write(f"{markdownify(str(content))}")
        except Exception as error:
            print(f"scraping with error: {error}")

    browser.close()
