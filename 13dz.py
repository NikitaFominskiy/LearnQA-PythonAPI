# import pytest
import requests

class TestUserAgent:
        def test_check_user_agent(self):
                header_req1 = {'user-Agent':'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
                header_req2 = {'user-Agent':'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'}
                header_req3 = {'user-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
                header_req4 = {'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'}
                header_req5 = {'user-Agent':'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

                response1 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                         headers=header_req1)
                response2 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                         headers=header_req2)
                response3 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                         headers=header_req3)
                response4 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                         headers=header_req4)
                response5 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                         headers=header_req5)

                header1 = {"platform": "Mobile", "browser": "No", "device": "Android", "user_agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
                header2 = {"platform": "Mobile", "browser": "Chrome", "device": "iOS", "user_agent":"Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"}
                header3 = {"platform": "Googlebot", "browser": "Unknown", "device": "Unknown", "user_agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
                header4 = {"platform": "Web", "browser": "Chrome", "device": "No", "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"}
                header5 = {"platform": "Mobile", "browser": "No", "device": "iPhone", "user_agent":"Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

                # response1 = response1.json()
                # response2 = response2.json()
                # response3 = response3.json()
                # response4 = response4.json()
                # response5 = response5.json()

                             # ({"user-Agent": header_req1}))

                assert response1.json() == header1, f"wrong headers"
                # assert response2.json() == header2, f"wrong headers"
                # assert response3.json() == header3, f"wrong headers"
                assert response4.json() == header4, f"wrong headers"
                # assert response5.json() == header5, f"wrong headers"

                # print(f"Cookie is {our_cookie}")





