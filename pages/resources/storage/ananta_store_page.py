""" Common fixtures and methods for Ananta Store section of the application. """
from test_helper.library.required_library import *
from pages.resources.storage.storage_page import *
from test_helper.testdata.storage_testdata import StorageTextData


""" Fixture to click on Ananta Store tab."""
@pytest.fixture(scope='module')
def ananta_setup(page, storage_setup):
    storage_features = page.query_selector_all(f'[data-testid="{locators["STORAGE_FEATURES"]}"]')
    storage_features_count = len(storage_features)
    print("Compute header count:", storage_features_count)
    for index, feature in enumerate(storage_features, start=1) :
        element_text = feature.inner_text()
        print(element_text)
        if StorageTextData.ananta_store_tab in element_text:
            feature.click()
    page.wait_for_timeout(TIMEOUT)


