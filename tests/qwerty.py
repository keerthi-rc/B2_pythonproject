import pytest
from playwright.async_api  import expect

# @pytest.mark.asyncio
# async def test_getbyrole(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     reg_link=async_page.get_by_role("link",name="Register")
#     await expect(reg_link).to_be_visible()
#     #click on it
#     await reg_link.click()
#     await async_page.wait_for_timeout(5000)
import pytest
from playwright.async_api import expect


# @pytest.mark.asyncio
# async def test_getByText(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#
#     excellent = async_page.get_by_role("radio", name="Excellent")
#
#     await expect(excellent).to_be_visible()
#     await expect(excellent).not_to_be_checked()
#
#     await excellent.click()
#
#     await expect(excellent).to_be_checked()
#
#
#
#     vb = async_page.get_by_role("radio", name="Very bad")
#
#     await expect(vb).to_be_visible()
#     await vb.click()



#
#
# @pytest.mark.asyncio
# async def test_getByText(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#
#     excellent = async_page.get_by_text("Excellent")
#     await expect(excellent).not_to_be_checked()
#     await excellent.click()
#     await expect(excellent).to_be_checked()
#
#
#     vb = async_page.get_by_role("radio", name="Very bad")
#     await expect(vb).to_be_visible()
#     await vb.click()
#     await async_page.wait_for_timeout(5000)

# @pytest.mark.asyncio
# async def test_getBylabel(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     reg_link = async_page.get_by_text("Register")
#     await expect(reg_link).to_be_visible()
#     await reg_link.click()
#     g=async_page.get_by_text("Male").nth(0)
#     await expect(g).to_be_visible()
#     await g.click()
#     fn=async_page.get_by_label("First name:")
#     await expect(fn).to_be_visible()
#     await fn.fill("Nevin")
#     ln=async_page.get_by_label("Last name:")
#     await expect(fn).to_be_visible()
#     await ln.fill("Jude Jose")
#     em=async_page.get_by_label("Email:")
#     await expect(em).to_be_visible()
#     await em.fill("nevin.jude@benzyinfotech.com")
#     pwd=async_page.get_by_label("Password:").nth(0)
#     await expect(pwd).to_be_visible()
#     await pwd.fill("Abc@123")
#     cpwd=async_page.get_by_label("Confirm Password:").nth(0)
#     await expect(cpwd).to_be_visible()
#     await cpwd.fill("Abc@123")
#     await async_page.wait_for_timeout(5000)

# page.getByPlaceholder() to locate an input by placeholder. working
# @pytest.mark.asyncio
# async def test_getByPlaceholder(async_page):
#    await async_page.goto("https://www.amazon.in/")
#    search_tb = async_page.get_by_placeholder("Search Amazon.in")
#    await expect(search_tb).to_be_visible()
#    await search_tb.fill("Books")
#    print(search_tb.input_value())
#    await async_page.wait_for_timeout(5000)

#page.getByAltText()
# @pytest.mark.asyncio
# async def test_getByAltText(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    img=async_page.get_by_alt_text("Picture of 14.1-inch Laptop")
#    await expect(img).to_be_visible()
#    await img.click()
#    await expect(async_page).to_have_url("https://demowebshop.tricentis.com/141-inch-laptop")
#    await async_page.wait_for_timeout(5000)

#page.getByTitle()
@pytest.mark.asyncio
async def test_getByTitle(async_page):
   await async_page.goto("https://demowebshop.tricentis.com/")
   img=async_page.get_by_title("Show details for Build your own cheap computer").nth(0)
   await expect(img).to_be_visible()
   await img.click()
   await expect(async_page).to_have_url("https://demowebshop.tricentis.com/build-your-cheap-own-computer")
   await async_page.wait_for_timeout(5000)
#
