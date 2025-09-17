import requests

methods = ["", "TRY", "POST","GET","PUT","DELETE", ]

for method in methods:

    response = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={'method': f"{method}"})
    print(f"GET request with parameter 'method' : {method}")
    print(f"Response code: {response.status_code}")
    print(f"Response text: {response.text}")
    print("-----------------")

    post_response = requests.post(
        "https://playground.learnqa.ru/api/compare_query_type", data={'method': f"{method}"})
    print(f"POST request with parameter 'method' : {method}")
    print(f"Response code: {post_response.status_code}")
    print(f"Response text: {post_response.text}")
    print("-----------------")

    put_response = requests.put(
        "https://playground.learnqa.ru/api/compare_query_type", data={'method': f"{method}"})
    print(f"PUT request with parameter 'method' : {method}")
    print(f"Response code: {put_response.status_code}")
    print(f"Response text: {put_response.text}")
    print("-----------------")

    delete_response = requests.delete(
        "https://playground.learnqa.ru/api/compare_query_type", data={'method': f"{method}"})
    print(f"DELETE request with parameter 'method' : {method}")
    print(f"Response code: {delete_response.status_code}")
    print(f"Response text: {delete_response.text}")
    print("-----------------")