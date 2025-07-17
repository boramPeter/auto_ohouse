import time,re,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from appium.webdriver.common.touch_action import TouchAction
import xml.etree.ElementTree as ET
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.common.exceptions import TimeoutException
import requests
from ozipsa.self_healing.self_healing_locator import SelfHealingUI


def is_session_active(driver):
    try:
        response = requests.get(f"{driver.command_executor._url}/session/{driver.session_id}")
        return response.status_code == 200
    except:
        return False

class ProviderCommonMethod:
    # 앱피움 공통 메서드 모아둠
    def __init__(self, driver):
        self.driver = driver
    def click(self, by_locator,desc=None):
        from mcp_automation.auto_locator_fix.AI_locator_handler import auto_repair_locator
        android_auto_flag = os.environ.get("ANDROID_AUTO_FLAG")
        ios_auto_flag = os.environ.get("IOS_AUTO_FLAG")
        xml_func = self.driver.page_source if android_auto_flag == "1" or ios_auto_flag == "1" else None
        if len(by_locator) == 3:
            method,locator,desc = by_locator
        else:
            method, locator = by_locator

        method = "xpath" if android_auto_flag == "1" or ios_auto_flag == "1" else method
        if desc is not None:
            try:
                ai_fix_locator = auto_repair_locator(locator,xml=xml_func)
                element = (method, ai_fix_locator)
                WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(element)).click()
            except Exception:
                healing_locator = SelfHealingUI.self_healing_locator(self,locator,desc)
                print(by_locator,healing_locator)
                auto_repair_locator(healing_locator,xml=xml_func)
                new_locator = (method,healing_locator)
                WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(new_locator)).click()

        else:
            ai_fix_locator = auto_repair_locator(locator,xml=xml_func)
            element = (method, ai_fix_locator)
            WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(element)).click()


    def long_click(self, by_locator, duration=1000):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)
        action_builder.pointer_action.move_to(element).pointer_down().pause(duration / 1500).pointer_up()
        action_builder.perform()

    def web_click(self, by_locator):
        self.driver.find_element_by_xpath(by_locator).click()

    def click_quick(self, by_locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).click()

    def capture_element_screenshot(self, by_locator, filename):
        element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(by_locator))
        element.screenshot(filename)

    def long_press(self, by_locator, duration=5000):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)
        action_builder.pointer_action.move_to(element).pointer_down().pause(duration / 1000).pointer_up()
        action_builder.perform()

    def send_key(self, by_locator, text):
        element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text)
    def web_send_key(self, by_locator, text):
        input_element = self.driver.find_element_by_xpath(by_locator)
        input_element.send_keys(text)

    def clear(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.clear()

    def get_text(self, by_locator,desc=None):
        from mcp_automation.auto_locator_fix.AI_locator_handler import auto_repair_locator
        android_auto_flag = os.environ.get("ANDROID_AUTO_FLAG")
        ios_auto_flag = os.environ.get("IOS_AUTO_FLAG")
        xml_func = self.driver.page_source if android_auto_flag == "1" or ios_auto_flag == "1" else None

        if len(by_locator) == 3:
            method,locator,desc = by_locator
        else:
            method, locator = by_locator
        method = "xpath" if android_auto_flag == "1" or ios_auto_flag == "1" else method

        if desc is not None:
            try:
                ai_fix_locator = auto_repair_locator(locator,xml=xml_func)
                element = (method, ai_fix_locator)
                element_locator = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(element))
            except Exception:
                healing_locator = SelfHealingUI.self_healing_locator(self,locator,desc)
                print(by_locator,healing_locator)
                auto_repair_locator(healing_locator,xml=xml_func)
                new_locator = (method,healing_locator)
                element_locator = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(new_locator))

        else:
            ai_fix_locator = auto_repair_locator(locator,xml=xml_func)
            element = (method, ai_fix_locator)
            print(element)
            element_locator = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(element))
        return element_locator.text

    def get_text_quick(self, by_locator):
        element = WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_name(self, by_locator,desc=None):
        from mcp_automation.auto_locator_fix.AI_locator_handler import auto_repair_locator
        android_auto_flag = os.environ.get("ANDROID_AUTO_FLAG")
        ios_auto_flag = os.environ.get("IOS_AUTO_FLAG")
        xml_func = self.driver.page_source if android_auto_flag == "1" or ios_auto_flag == "1" else None

        if len(by_locator) == 3:
            method,locator,desc = by_locator
        else:
            method, locator = by_locator

        method = "xpath" if android_auto_flag == "1" or ios_auto_flag == "1" else method

        if desc is not None:
            try:
                ai_fix_locator = auto_repair_locator(locator, xml=xml_func)
                element = (method, ai_fix_locator)
                element_locator = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(element))
            except Exception:
                healing_locator = SelfHealingUI.self_healing_locator(self, locator, desc)
                print(by_locator, healing_locator)
                auto_repair_locator(healing_locator, xml=xml_func)
                new_locator = (method, healing_locator)
                element_locator = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(new_locator))

        else:
            ai_fix_locator = auto_repair_locator(locator, xml=xml_func)
            element = (method, ai_fix_locator)
            print(element)
            element_locator = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(element))
        return element_locator.get_attribute('name')

    def get_name_quick(self, by_locator):
        element = WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute('name')

    def get_value(self, by_locator):
        element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute('value')
    
    def get_content_desc(self, by_locator):
        element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute('content-desc')

    def is_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(by_locator))
        element.is_displayed()

    def is_enabled(self, by_locator,desc=None):
        from mcp_automation.auto_locator_fix.AI_locator_handler import auto_repair_locator
        android_auto_flag = os.environ.get("ANDROID_AUTO_FLAG")
        ios_auto_flag = os.environ.get("IOS_AUTO_FLAG")
        xml_func = self.driver.page_source if android_auto_flag == "1" or ios_auto_flag == "1" else None
        if len(by_locator) == 3:
            method,locator,desc = by_locator
        else:
            method, locator = by_locator

        method = "xpath" if android_auto_flag == "1" or ios_auto_flag == "1" else method

        if desc is not None:
            try:
                ai_fix_locator = auto_repair_locator(locator, xml=xml_func)
                element = (method, ai_fix_locator)
                element_locator = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(element))
            except Exception:
                healing_locator = SelfHealingUI.self_healing_locator(self, locator, desc)
                print(by_locator, healing_locator)
                auto_repair_locator(healing_locator, xml=xml_func)
                new_locator = (method, healing_locator)
                element_locator = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(new_locator))

        else:
            ai_fix_locator = auto_repair_locator(locator, xml=xml_func)
            element = (method, ai_fix_locator)
            print(element)
            element_locator = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(element))
        return element_locator.is_enabled()

    def is_checked(self, by_locator):
        element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(by_locator))
        return str(element.get_attribute('checked')).capitalize()

    def is_enabled_quick(self, by_locator,desc=None):
        from mcp_automation.auto_locator_fix.AI_locator_handler import auto_repair_locator
        android_auto_flag = os.environ.get("ANDROID_AUTO_FLAG")
        ios_auto_flag = os.environ.get("IOS_AUTO_FLAG")
        xml_func = self.driver.page_source if android_auto_flag == "1" or ios_auto_flag == "1" else None
        if len(by_locator) == 3:
            method, locator, desc = by_locator
        else:
            method, locator = by_locator

        method = "xpath" if android_auto_flag == "1" or ios_auto_flag == "1" else method

        if desc is not None:
            try:
                ai_fix_locator = auto_repair_locator(locator, xml=xml_func)
                element = (method, ai_fix_locator)
                element_locator = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(element))
            except Exception:
                healing_locator = SelfHealingUI.self_healing_locator(self, locator, desc)
                print(by_locator, healing_locator)
                auto_repair_locator(healing_locator, xml=xml_func)
                new_locator = (method, healing_locator)
                element_locator = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(new_locator))

        else:
            ai_fix_locator = auto_repair_locator(locator, xml=xml_func)
            element = (method, ai_fix_locator)
            print(element)
            element_locator = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(element))
        return element_locator.is_enabled()

    def is_selected(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.is_selected()

    def get_location_xy(self, by_locator, desc=None):
        from mcp_automation.auto_locator_fix.AI_locator_handler import auto_repair_locator
        android_auto_flag = os.environ.get("ANDROID_AUTO_FLAG")
        ios_auto_flag = os.environ.get("IOS_AUTO_FLAG")
        xml_func = self.driver.page_source if android_auto_flag == "1" or ios_auto_flag == "1" else None
        if len(by_locator) == 3:
            method, locator, desc = by_locator
        else:
            method, locator = by_locator

        method = "xpath" if android_auto_flag == "1" or ios_auto_flag == "1" else method

        if desc is not None:
            try:
                ai_fix_locator = auto_repair_locator(locator, xml=xml_func)
                asis_locator = (method, ai_fix_locator)
                element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(asis_locator))
            except Exception:
                healing_locator = SelfHealingUI.self_healing_locator(self, locator, desc)
                print(by_locator, healing_locator)
                auto_repair_locator(healing_locator, xml=xml_func)
                new_locator = (method, healing_locator)
                element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(new_locator))

        else:
            ai_fix_locator = auto_repair_locator(locator, xml=xml_func)
            asis_locator = (method, ai_fix_locator)
            print(asis_locator)
            element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(asis_locator))
        location = element.location
        x = int(location['x'])
        y = int(location['y'])
        print(f'get_location_xy : {x, y}')
        return [x, y]


    
    def get_bounds(self, by_locator):
        element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(by_locator))
        location = element.location
        x = int(location['x'])
        y = int(location['y'])
        
        size = element.size
        w = x + int(size['width'])
        h = y + int(size['height'])
        
        print(f'get_bounds : {x,y,w,h}')
        
        return[x, y, w, h]

    def get_height(self, by_locator):
        element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(by_locator))

        height = element.size['height']
        print(f"Element height: {height}")

        return height

    def switch_to_native(self):
        # contexts = self.driver.contexts
        navtive_context = "NATIVE_APP"
        self.driver.switch_to.context(navtive_context)
        print(navtive_context)

    def switch_to_webview(self):
        contexts = self.driver.contexts
        webview_context = contexts[1]
        self.driver.switch_to.context(webview_context)
        print(webview_context)

    def assert_equal(self, expected_result, actual_result):
        assert actual_result == expected_result, f"기대 결과: {expected_result}, 실제 결과: {actual_result}"

    def assert_in(self, expected_texts, actual_result):
        assert expected_texts in actual_result, f"기대 결과: {expected_texts}, 실제 결과: {actual_result}"

    def assert_in_2(self, expected_texts, actual_result):
        assert actual_result in expected_texts, f"기대 결과: {expected_texts}, 실제 결과: {actual_result}"

    def assert_in_list(self, expected_texts, actual_result):
        assert all(any(str(expected_item) in str(actual_item) for actual_item in actual_result) for expected_item in
                   expected_texts), f"기대 결과: {expected_texts}, 실제 결과: {actual_result}"

    def get_xml_depth(self):
        xml_content = self.driver.page_source
        xml_depth = len(re.findall(r'<(?!.*com\.android\.systemui:id/)', xml_content))
        return xml_depth

    def get_xml(self):
        return self.driver.page_source

    def find_xml_text(self, search_string, retries=3, delay=0.5):
        for attempt in range(retries):
            try:
                page_source = self.driver.page_source
                if search_string in page_source:
                    return True
            except Exception as e:
                print(f"페이지 소스 로드 실패 (시도 {attempt + 1}/{retries}): {e}")
            time.sleep(delay)

        raise TimeoutException(f"'{search_string}' 문자열이 page_source 내에 존재하지 않습니다.")
    def count_img_xml_class(self, platform):
        try:
            image_class = ".//XCUIElementTypeImage" if platform == "iOS" else ".//android.widget.ImageView"
            xml_content = self.driver.page_source
            root = ET.fromstring(xml_content)

            count = 0
            for _ in root.findall(image_class):
                count += 1

            print(count)
            return count
        except Exception as e:
            print(f"요소 count_img_xml_class 갯수 세는 과정에서 에러 발생. 1개로 리턴해서 케이스 진행 : {e}")
            return 1

    def count_xml_class(self, platform):
        try:
            common_class = ".//XCUIElementTypeStaticText" if platform == "iOS" else ".//android.widget.TextView"
            xml_content = self.driver.page_source
            root = ET.fromstring(xml_content)

            count = 0
            for element in root.findall(common_class):
                if platform == "iOS":
                    text = element.get('name')
                else:
                    text = element.get('text')

                if text and len(text) > 1:
                    count += 1

            print(count)
            return count

        except Exception as e:
            print(f"요소 count_xml_class 갯수 세는 과정에서 에러 발생. 1개로 리턴해서 케이스 진행 : {e}")
            return 1
    
    def get_screen_size(self):
        size = self.driver.get_window_size()
        return [size['width'], size['height']]

    '''
    1. 안드 pdp 네트워크 에러뜰경우, 다 제거하고 105개 뎁스정도임 + 광고 pdp에선 89였음 + 광고 pdp에서 93인 경우도있음
        1-1. 쇼핑홈쪽은 125임. 화면별로 정리가 필요함
    2. 안드 o2o쪽은 전반적으로 뎁스가 적다.
    3. ios는 새창이 뜬다면 뎁스가 늘어난다. (측정기준을 함수별로 체크해야될것같다)
    ㄴ> 필수 클래스를 검색하는게 나아보임. 하나하나 조건거는게 불편해보인다.
    아이폰 기준 공통은 5개, 그 외에는 20개로
    안드도 7, 그외에는 20개정도로 하면될거같음
    '''
class ProviderScrollMethod:
    # 스크롤만 전용으로 빼둠
    def __init__(self, driver, actions):
        self.driver = driver
        self.actions = actions

    def up_scroll(self):
        device_size = self.driver.get_window_size()
        screen_width = device_size['width']
        screen_height = device_size['height']

        start_x = screen_width / 2
        end_x = screen_width / 2
        start_y = screen_height / 4
        end_y = screen_height / 3
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)

    def up_scroll2(self):
        device_size = self.driver.get_window_size()
        screen_width = device_size['width']
        screen_height = device_size['height']
        start_x = screen_width / 2
        end_x = screen_width / 2
        start_y = screen_height / 5
        end_y = screen_height / 3

        self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)

    def down_scroll(self):
        device_size = self.driver.get_window_size()
        screen_width = device_size['width']
        screen_height = device_size['height']
        start_x = screen_width / 2
        end_x = screen_width / 2
        start_y = screen_height * 6 / 9
        end_y = screen_height / 5

        self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)


    def down_scroll2(self):
        device_size = self.driver.get_window_size()
        screen_width = device_size['width']
        screen_height = device_size['height']
        start_x = screen_width / 2
        end_x = screen_width / 2
        start_y = (screen_height * 2) / 3
        end_y = screen_height / 2

        self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)

    def down_scroll3(self):
        device_size = self.driver.get_window_size()
        screen_width = device_size['width']
        screen_height = device_size['height']
        start_x = screen_width / 2
        end_x = screen_width / 2
        start_y = (screen_height * 3) / 4
        end_y = screen_height / 2

        self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)

    def down_scroll_o2o(self):
        device_size = self.driver.get_window_size()
        screen_width = device_size['width']
        screen_height = device_size['height']
        start_x = screen_width / 2
        end_x = screen_width / 2
        start_y = screen_height * 7 / 9
        end_y = screen_height / 9
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)


    def pull_to_refresh(self):


        device_size = self.driver.get_window_size()
        screen_width = device_size['width']
        screen_height = device_size['height']

        start_x = screen_width / 2
        end_x = screen_width / 2
        start_y = screen_height * 2 / 10
        end_y = screen_height * 7 / 10

        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)

        duration = 5000

        action_builder.pointer_action.move_to_location(start_x, start_y)
        action_builder.pointer_action.pointer_down()
        action_builder.pointer_action.pause(duration / 1000)
        action_builder.pointer_action.move_to_location(end_x, end_y)
        action_builder.pointer_action.pointer_up()

        action_builder.perform()


    def to_right_swipe(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        start_x = int(width * 0.2)
        end_x = int(width * 0.8)
        y = int(height * 0.3)
        # self.actions = TouchAction(self.driver)
        # self.actions.press(x=start_x, y=y).wait(2000).move_to(x=end_x, y=y).release()
        # self.actions.perform()
        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)

        action_builder.pointer_action.move_to_location(start_x, y)
        action_builder.pointer_action.pointer_down()
        action_builder.pointer_action.move_to_location(end_x, y)
        action_builder.pointer_action.pointer_up()

        action_builder.perform()

    def to_left_swipe(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        start_x = int(width * 0.8)
        end_x = int(width * 0.2)
        y = int(height * 0.3)


        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)

        action_builder.pointer_action.move_to_location(start_x, y)
        action_builder.pointer_action.pointer_down()
        action_builder.pointer_action.move_to_location(end_x, y)
        action_builder.pointer_action.pointer_up()

        action_builder.perform()


    def xy_click(self, x, y):
        print(f'요소_좌표_클릭 : {x,y}')
        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)
        action_builder.pointer_action.move_to_location(x, y).click()
        action_builder.perform()

    #device size - 좌표 위치 클릭
    def xy_click_size(self,x_rate,y_rate):
        device_size = self.driver.get_window_size()
        screen_width = device_size['width']
        screen_height = device_size['height']  
        x = int(screen_width * x_rate)
        y = int(screen_height * y_rate )  
        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)
        action_builder.pointer_action.move_to_location(x, y).click()
        action_builder.perform()


    def xy_scroll(self, start_x, start_y, end_x, end_y):

        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)

        action_builder.pointer_action.move_to_location(start_x, start_y)
        action_builder.pointer_action.pointer_down()
        action_builder.pointer_action.move_to_location(end_x, end_y)
        action_builder.pointer_action.pointer_up()

        action_builder.perform()

    def xy_scroll2(self, start_x, start_y, end_x, end_y):

        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)

        action_builder.pointer_action.move_to_location(start_x, start_y)
        action_builder.pointer_action.pointer_down()
        action_builder.pointer_action.move_to_location(end_x, end_y)
        action_builder.pointer_action.pointer_up()

        action_builder.perform()

    def xy_scroll2_ios(self, start_x, start_y, end_x, end_y):

        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self.driver, mouse=pointer_input)

        action_builder.pointer_action.move_to_location(start_x, start_y)
        action_builder.pointer_action.pointer_down()
        action_builder.pointer_action.move_to_location(end_x, end_y)
        action_builder.pointer_action.pointer_up()

        action_builder.perform()

    def xy_swipe(self, start_x, start_y, end_x, end_y):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)

    def enter_key(self):
        self.driver.press_keycode(66)

    def back_key(self):
        self.driver.press_keycode(4)

    def open_noti(self):
        self.driver.open_notifications()

