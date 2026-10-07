f # import pytest
# from playwright.async_api  import expect
#
# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     ele=async_page.get_by_text("from playwright.async_api  import expect")
#     await expect(ele).to_be_visible()
from email.mime import text
from pkgutil import extend_path
from pydoc import html
from tokenize import group

import pytest
from playwright.async_api import expect
from pygments.lexers import css


# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    ele = async_page.locator("h2[class='topic-html-content-header']")
#    await expect(ele).to_be_visible()
#    print(await ele.inner_text())
#------------------ Welcome to our store
#CSS
#tab_name[an='av']
#if we have id attribute
# #id_value
# if multiple element selecting, we want single ele is not applicable
# *  - Contains
#h2[aria-label*="Samsung"]
# ^  - starts with
# $ - ends with


# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    ele = async_page.locator("h2[class='topic-html-content-header']")
#    await expect(ele).to_be_visible()
#    print(await ele.inner_text())

# if we have class
#     .class_name
#not allowed to use space between the class name attribute
# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/books")
   # ele = async_page.locator(".product-title").nth(0)
   # await expect(ele).to_be_visible()
   # print(await ele.inner_text())
   #To print all products
   # ele = async_page.locator(".product-title")# ele store all products
   # all_product= await ele.all()
   # for i in all_product:
   #     print(await i.inner_text())

#Ashwini code
# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/books")
#    ele = async_page.locator(".product-title") # locator :notfinding
#    # ele :-- all products
#    all_product = await ele.all()
#    for i in all_product:
#        print(await i.inner_text())

# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#     await async_page.goto("https://www.amazon.com/")
#     ele=async_page.locator("#twotabsearchtextbox")
#    await ele.fill("Books")

@pytest.mark.asyncio
async def test_getBytitle(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    ele=async_page.locator("input[class='button-2 product-box-add-to-cart-button']")
    all_product=await ele.all()
    for i in all_product:
        await i.click()
        break
    await async_page.wait_for_timeout(5000)

# if multiple element selecting, we want single ele is not applicable
#Xpaths
#Based on the product name i want to click on product

# pr_name="14.1-inch Laptop"
# xpath=""

# Xpath:-->
# (/) Absolute Xpath
# html
#     <body>
#     <div>
#         <input>A
#         <input>B
#     <div>
#         <input>C
#         <input>D

# /html/body/div[1]/input[1]
# (//)Relative Xpath
#
# #xpath by attribute
# //tag_name[@an='av']
#
# # xpath by text
# //tag_name[text()='text']
#
# # xpath by contains
# //tag_name[contains(an,'av')]
# //tag_name[contains(text(),text)]
#
# # xpath by group
#     (xpath)[index_num]

# xpath
# //input[@name='email']
# css
# input[@name='email']

 # input[aria-label="Add to cart"] -- not possible to get one from 27 outputs
# (//input[@aria-label="Add to cart"])[1]

# //table[@class='ui-datepicker-calendar']/thead/tr/th
# //table[@class='ui-datepicker-calendar']/thead/tr/.. #moving back to parent
#
# //a[@class='ui-state-default ui-state-hover']/..
