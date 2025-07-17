import unittest,warnings
from appium import webdriver
from app.common.app_config.data import PackageName
from app.common.app_config.data import ChromeDriverPath


class WebDriver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '13.0',
            'appPackage': PackageName.aos_package_name,
            'appActivity': 'se.ohou.screen.splash.SplashActivity',
            "automationName": "uiautomator2",
            'noReset': True,
            "enableMultiWindows": True,
            "chromedriverExecutable": ChromeDriverPath.chrome_driver_path
        }

        warnings.simplefilter("ignore")
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(10)

        print('setUpClass 완료')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('tearDownClass 완료')

    def setUp(self):
        print('setUp 완료')

    def tearDown(self):
        print('tearDown 완료')

    if __name__ == '__main__':
        unittest.main()