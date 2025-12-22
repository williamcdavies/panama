from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    """
    Docstring for run
    
    :param playwright: Description
    :type playwright: Playwright
    """

    
    chromium = playwright.chromium
    browser  = chromium.launch()
    page     = browser.new_page()
    
    # pipe

    browser.close()


with sync_playwright() as playwright:
    run(playwright)