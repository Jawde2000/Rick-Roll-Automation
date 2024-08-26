import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.youtube.com/")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("Search").fill("never gonna give you up")
    page.get_by_role("button", name="Search", exact=True).wait_for(state="visible")
    button = page.get_by_role("button", name="Search", exact=True)
    if button.is_enabled():
        button.click(button="left")
    else:
        print("Button is disabled.")
    page.get_by_role("button", name="Search", exact=True).click()
    page.wait_for_load_state("networkidle")
    page.get_by_role("heading", name="Rick Astley - Never Gonna Give You Up (Official Music Video) by Rick Astley 1,").locator("#video-title").click(button="left")
    page.get_by_role("heading", name="Rick Astley - Never Gonna Give You Up (Official Music Video) by Rick Astley 1,").locator("#video-title").click()

    time.sleep(213)
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)