
def perform_click_on_tejas_tab(page, selector, timeout=1000):
    page.wait_for_timeout(timeout)
    page.wait_for_selector(selector).click()

def perform_click_on_create_vm_button(page, selector, timeout=1000):
    page.wait_for_timeout(timeout)
    page.wait_for_selector(selector).click()
