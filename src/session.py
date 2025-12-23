from playwright.sync_api import Playwright, sync_playwright


def _run(playwright: Playwright):
    """
    Docstring for _run
    
    :param playwright: Description
    :type playwright: Playwright
    """


    chromium = playwright.chromium
    browser  = chromium.launch()
    page     = browser.new_page()
    page.goto("https://chatgpt.com/")

    browser.close()


def run():
    """
    Docstring for run
    """


    with sync_playwright() as playwright:
        _run(playwright)