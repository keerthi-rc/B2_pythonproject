# import pytest
# from tests.utils.config import BASE_URL
#
#
# @pytest.mark.asyncio
# async def test_env(async_page):
#     await async_page.goto(BASE_URL)
#     print(await async_page.title())
import pytest
from playwright.async_api  import expect

@pytest.mark.asyncio
async def test_getbyrole(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    reg_link=async_page.get_by_role("link",name="Register")
    await expect(reg_link).to_be_visible()
    #click on it
    await reg_link.click()