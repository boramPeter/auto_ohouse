import inspect, os, re
import threading


class ProviderFunctionName:
    thread_local = threading.local()
    def get_current_function_name(self,scenario=None, st_rt=None,platform=None):
        self.thread_local.scenario = None
        self.thread_local.st_rt = None

        self.thread_local.scenario = scenario
        self.thread_local.st_rt = st_rt

        function_name = inspect.currentframe().f_back.f_code.co_name
        if self.thread_local.scenario is not None:

            function_parts = function_name.split("test_")[1].split(platform)[0]
            func_name_scenario = re.search(r'\b\w*\d{5}(?=\s)', self.thread_local.scenario).group(0)
            function_name_replace = function_name.replace(function_parts, func_name_scenario)

            print(f"scenario,st_rt,func,dir: {self.thread_local.scenario}, {self.thread_local.st_rt},{function_name},{platform}")

            if self.thread_local.st_rt and any(x in function_name_replace for x in ["step", "check"]):
                print("if self.thread_local.st_rt condition pass")

                st_rt_value = "rt" if self.thread_local.st_rt[0] == "RT" else "st_rt"
                function_name_replace = function_name_replace.replace("step", f"{st_rt_value}_step").replace("check",
                                                                                                             f"{st_rt_value}_check")

            print(f"function_name: {function_name_replace}")
            return function_name_replace

        return function_name