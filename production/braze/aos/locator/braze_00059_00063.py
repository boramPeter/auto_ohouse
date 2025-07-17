from appium.webdriver.common.appiumby import AppiumBy
from app.common.base_method.appium_method import ProviderCommonMethod


class ProviderBrazeLocator(ProviderCommonMethod):
    available_tab = (AppiumBy.XPATH, '//android.widget.TextView[@text="AVAILABLE (2)"]')

    ohouse_btn = (AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.deploygate:id/app_author"])[1]')

    package_archive_btn = (AppiumBy.ID, 'com.deploygate:id/app_revisions_button')

    def version_name(idx):
        version_name = (
        AppiumBy.XPATH, f'(//android.widget.TextView[@resource-id="com.deploygate:id/iar__version"])[{idx}]')
        return version_name
