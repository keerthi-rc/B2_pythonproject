# from playwright.async_api import async_playwright
# import pytest
#
# # @pytest.mark.asyncio
# # def test_diff_pages(async_page):
#
# @pytest.mark.asyncio
# async def test_diff_browser():
#  # ----------------------chrome-----------------------#
#     async with async_playwright() as p:
#         chrome_browser=await p.chromium.launch(headless=False)
#         user_context=await chrome_browser.new_context()
#         page= await user_context.new_page()
#         await page.goto("https://www.google.com")
#         await page.wait_for_timeout(5000)
#
#
#         admin_context=await chrome_browser.new_context()
#         page=await admin_context.new_page()
#         await page.goto("https://www.amazon.in")
#         await page.wait_for_timeout(5000)
# #--------------------------firefox----------------------#
#         firefox_browser = await p.firefox.launch(headless=False)
#         user_context = await firefox_browser.new_context()
#         page = await user_context.new_page()
#         await page.goto("https://www.google.com")
#         await page.wait_for_timeout(5000)
#
#
#         admin_context = await firefox_browser.new_context()
#         page = await admin_context.new_page()
#         await page.goto("https://www.amazon.in")

import pytest

@pytest.mark.asyncio
@pytest.mark.smoke
async def test_chrome_browser(chromium_page):
    await chromium_page.goto("https://www.google.com")

@pytest.mark.asyncio
@pytest.mark.regression
async def test_firefox_browser(firefox_page):
    await firefox_page.goto("https://www.google.com")

@pytest.mark.asyncio
async def test_webkit_page(webkit_page):
    await webkit_page.goto("https://www.google.com")
