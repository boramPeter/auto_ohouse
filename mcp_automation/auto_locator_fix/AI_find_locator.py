# -*- coding: utf-8 -*-

from google import genai
import time,os,re
from selenium.common.exceptions import TimeoutException

class HealingUiLocator:
    def find_locator(self,locator,page_source=None):
        client = genai.Client(api_key="AIzaSyBJXmuqL1lBC3lHM9WmwDJDgbBBZzUtGAw")
        # from app.common.base_method.appium_method import ProviderCommonMethod
        input_text = f'''
        You are an AI assistant specialized in analyzing XML UI structures and generating Appium XPaths.

        **Input:**
        * `locator`: An existing XPath string (potentially outdated): `{locator}`
        * `page_source`: The current XML page source as a string:
            ```xml
            {page_source}
            ```
        
        **Task:**
        Your goal is to find the single best matching UI element in the provided `{page_source}` corresponding to the original `{locator}`, prioritizing elements that are currently visible, and return a valid Appium XPath for it.
        
        **Execution Steps:**
        
        1.  **Filter for Visibility:** First, mentally (or algorithmically) filter the `{page_source}` to consider *only* XML elements where the `@visible` or `@displayed` attribute is equal to 'true'. All subsequent search steps operate *only* on these visible elements.
        
        2.  **Check Exact Locator:** Verify if the exact `{locator}` path exists within the filtered visible elements of `{page_source}`. If it exists and points to a visible element, construct an Appium-compatible XPath ensuring it includes `[@visible='true']` or `[@displayed='true']`. If this condition is met, return this XPath.
        
        3.  **Name/Text Match:**
            a.  If Step 2 fails, parse the original `{locator}` to extract any `@name` or `@text` attribute conditions.
            b.  If `@name` or `@text` is found, search *only the visible elements* in `{page_source}` for an element with the *exact same* `@name` or `@text` value. If a unique match is found, construct a new, robust Appium XPath (starting with `//`) for this element, incorporating `[@visible='true']` or `[@displayed='true']` and potentially other stable attributes like `resource-id`, `content-desc`, or `class` if available in the matched element. Return this XPath.
            c.  If no exact match is found (but `@name`/`@text` was present in the original locator), attempt a *semantic match*. Find the visible element in `{page_source}` whose `@name` or `@text` seems *most similar in meaning* to the original. Construct and return a robust Appium XPath for this best-guess element, including the visibility condition.
        
        4.  **Coordinate Match:**
            a.  If Steps 2 and 3 fail, check if the original `{locator}` contained coordinate information (e.g., `@x`, `@y`, or `bounds`).
            b.  If coordinates are found, identify the approximate location. Search *only the visible elements* in `{page_source}` to find the element geometrically *closest* to these coordinates.
            c.  Construct and return a robust Appium XPath for this element, including the visibility condition.
        
        5.  **Hierarchical/Structural Match:** If no element is found via the above steps, analyze the structure (parent/child/sibling relationships) implied by the original `{locator}`. Find the visible element in `{page_source}` that resides in the *most similar structural position*. Construct and return a robust Appium XPath for this element, including the visibility condition.
        
        6.  **Final XPath Generation and Validation:**
            * Based on the successful step (2-5), generate the *single best* Appium XPath.
            * **Crucially:** The generated XPath **must**:
                * Start with `//`.
                * Be syntactically valid for Appium.
                * Include a condition like `[@visible='true']` or `[@displayed='true']`. (Choose one based on the source's attribute naming).
            * If multiple potential candidates arise during a step, use heuristics (e.g., prefer elements with unique IDs, shorter paths, closer structural similarity) to select the single most probable match.
        **--- CRITICAL OUTPUT INSTRUCTION ---**
        **Your response MUST be ONLY the raw XPath string itself.**
        * **DO NOT** wrap the XPath in markdown code blocks (like ```xpath ... ``` or ``` ... ```).
        * **DO NOT** include ANY introductory text (e.g., "Here is the XPath:", "The resulting XPath is:").
        * **DO NOT** include ANY explanatory text or comments.
        * **DO NOT** include ANY characters before the `//` at the beginning of the XPath.
        * **DO NOT** include ANY characters (including newlines) after the final `]` of the XPath.
        * The ENTIRE response MUST be the XPath string, starting with `//`.
        
        **Example of CORRECT Output:**
        `//android.widget.TextView[@resource-id='com.example.app:id/title'][@text='Welcome'][@displayed='true']`
        
        **Examples of INCORRECT Output:**
        * ` ```xpath\n//android.widget.TextView[...]\n``` `
        * ` The XPath is: //android.widget.TextView[...] `
        * ` //android.widget.TextView[...] (found using text match) `
        **Output Requirement:**
        * Your response **MUST** contain **ONLY** the final generated XPath string.
        * Do **NOT** include any explanations, introductory text, code formatting markers, or any other characters before or after the XPath string itself.
        * Example valid output: `//android.widget.TextView[@resource-id='com.example.app:id/title'][@text='Welcome'][@displayed='true']`
        
        **Process the input `locator` and `page_source` now based on these instructions.**
        '''
        '''
        보안을 위해 프롬프트 외엔 제거
        '''
