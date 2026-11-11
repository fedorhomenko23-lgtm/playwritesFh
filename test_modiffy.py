# Хоменко Фёдор Витальевич
# 11.11.26
# 17:10
# Страницы изолированы между тестами благодаря контексту браузера , который эквивалентен совершенно новому профилю браузера, где каждый тест получает новую среду, даже если несколько тестов запускаются в одном браузере.

import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield
    
    print("after the test runs")

def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")