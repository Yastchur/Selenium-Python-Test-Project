from pages.product_page import ProductPage
import pytest

promo_links = [
    '?promo=offer0',
    '?promo=offer1',
    '?promo=offer2',
    '?promo=offer3',
    '?promo=offer4',
    '?promo=offer5',
    '?promo=offer6',
    pytest.param('?promo=offer7', marks=pytest.mark.xfail(reason="some bug")),
    '?promo=offer8',
    '?promo=offer9',
]

@pytest.mark.parametrize("promo", promo_links)
def test_guest_can_add_product_to_basket(browser, promo):    
    base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    url = f"{base}{promo}"
    page = ProductPage(browser, url)
    page.open()
    page.add_product_to_basket()
    page.should_be_correct_product_in_basket()
    page.should_be_correct_price_in_basket()
