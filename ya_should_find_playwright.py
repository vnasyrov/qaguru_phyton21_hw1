from playwright.sync_api import sync_playwright, expect

def test_input_value():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://ya.ru')
        page.fill('input#text', 'погода спб')
        page.press('input#text', 'Enter')

        # Проверяем, что поле ввода содержит нужное значение
        expect(page.locator('input[name="text"]')).to_have_value('погода спб')

        browser.close()
