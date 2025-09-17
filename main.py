import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect",)
print(f"Count: {len(response.history)}")
print(f"Final URL: {response.url}")