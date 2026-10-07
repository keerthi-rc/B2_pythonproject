# from playwright.sync_api import expect, sync_playwright
# def test_async_sync_exp1():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         user_context = browser.new_context()
#         page = user_context.new_page()
#         page.goto("https://www.facebook.com/")
#         print(page.title())
#         expect(page).to_have_title("Facebook")
#
from playwright.sync_api import expect, sync_playwright


import asyncio
from playwright.async_api import expect, async_playwright


async def test_async_sync_exp1():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        user_context = await browser.new_context()
        page = await user_context.new_page()

        await page.goto("https://www.facebook.com/")
        print(await page.title())

        await expect(page).to_have_title("Facebook")

        await browser.close()


asyncio.run(test_async_sync_exp1())