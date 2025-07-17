import unittest
import warnings
from appium import webdriver
from app.common.app_config.data import UDID
from app.common.app_config.data import XcodeOrgId
from app.common.app_config.data import PackageName


class IosWebDriver(unittest.TestCase):
    driver = None
    
    
    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'iOS',
            'platformVersion': '16.4.1',
            'automationName': 'XCUITest',
            'deviceName': 'iPhone',
            'udid': UDID.iphone12mini_udid,
            'xcodeOrgId': XcodeOrgId.team_orgid,
            'bundleId': PackageName.ios_bundle_id,
            'noReset': True
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
