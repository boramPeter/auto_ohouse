# running_value_provider.py

import time
import threading

class CacheManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.cache_data = {}
                    cls._instance.cache_expiration = {}
        return cls._instance

    def set(self, key, value):
        with self._lock:
            self.cache_data[key] = value
            self.cache_expiration[key] = time.time() + (3 * 3600)

    def get(self, key):
        with self._lock:
            if key in self.cache_data:
                if time.time() < self.cache_expiration[key]:
                    return self.cache_data[key]
                else:
                    del self.cache_data[key]
                    del self.cache_expiration[key]
            return None
