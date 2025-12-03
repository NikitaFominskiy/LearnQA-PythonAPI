# import pytest
import requests

class TestCookie:
        def test_check_cookie(self):
                response1 = requests.get("https://playground.learnqa.ru/api/get_cookie")
                our_cookie = dict(response1.cookies)
                expected_cookie = {'MyCookie': '12345'}
                assert our_cookie == expected_cookie, f"ne to"
                print(f"Cookie is {our_cookie}")
# print(dict(our_cookie))