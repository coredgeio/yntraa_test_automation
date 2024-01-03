

def perform_click_compute_resource(page, selector, timeout=3000):
    page.wait_for_timeout(timeout)
    page.wait_for_selector(selector).click()
    actual_text = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
    print(f"Heading in the section: {actual_text}")
    return actual_text
