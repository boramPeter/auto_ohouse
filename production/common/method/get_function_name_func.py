import inspect, re, os
class ProviderFunctionName:
    def get_current_function_name(self,scenario=None):
        function_name = inspect.currentframe().f_back.f_code.co_name
        if scenario is not None:
            current_dir = os.getcwd()
            if "ios" in current_dir:
                platform = "_ios"
            elif "android" in current_dir:
                platform = "_aos"
            else:
                platform = "_web"
            function_parts = function_name.split("prod_")[1].split(platform)[0]
            func_name_scenario = re.search(r'\b\w*\d{5}(?=\s)', scenario).group(0)
            function_name_replace = function_name.replace(function_parts,func_name_scenario)
            print(f"function_name:{function_name_replace}")
            return function_name_replace
        return function_name
