# -*- coding: utf-8 -*-
# @Author : 艾登Aiden
# @Email : aiden2048@qq.com
# @Date : 2022-04-07

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from wirebrowserenv.wirebrowserenv import WireBrowserEnv

class DemoEnv(object):

    def __init__(self, *arg, **kwargs):
        self.set_params()
        self.env = WireBrowserEnv(
            url=self.url, 

            intercept_enabled=self.intercept_enabled, 
            intercept_url=self.intercept_url, 
            intercept_mode=self.intercept_mode,
            intercept_params=self.intercept_params,

            headless=self.headless, 
            images_enabled=self.images_enabled, 
            incognito=self.incognito, 
            stealth=self.stealth, 
            proxy=self.proxy, 
            time_delay=self.time_delay, 
            timeout=self.timeout, 
        )

    def __del__(self):
        if self.intercept_enabled:
            self.env.driver.close()

    def set_params(self):
        self.headless = False
        self.images_enabled = False
        self.incognito = False
        self.stealth = False
        self.proxy = None
        self.time_delay = 0
        self.timeout = 20

        self.intercept_enabled = True

        self.url = 'https://httpbin.org/ip'

        self.intercept_url = 'https://httpbin.org/ip'
        insert_text = '这是已经替换的页面'
        split_word = '.'
        starts_word = '135'
        self.script = 'return window.document.body.innerHTML'

        self.intercept_mode = 'modify'
        self.intercept_params={
            'modify_insert_text': insert_text,
            'modify_split_word': split_word,
            'modify_starts_word': starts_word,
        }

    def get_result(self):
        result = self.env.execute_script(self.script)
        return result if result else ''


if __name__ == "__main__":
    for _ in range(1):
        env = DemoEnv()
        result = env.get_result()
        print(result)