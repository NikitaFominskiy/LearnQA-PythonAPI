import requests
import pytest

def test_check_headers():
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        headers = response.headers
        print("\nПолученные заголовки:")
        for header, value in headers.items():
            print(f"{header}: {value}")

        assert "Date" in headers, "There is no Date in response"
        assert "Content-Type" in headers, "There is no Content-Type in response"
        assert "Content-Length" in headers, "There is no Content-Length in response"
        assert "Connection" in headers, "There is no Connection in response"
        assert "Keep-Alive" in headers, "There is no Keep-Alive in response"
        assert "Server" in headers, "There is no Server in response"
        assert "x-secret-homework-header" in headers, "There is no x-secret-homework-header in response"
        assert "Cache-Control" in headers, "There is no Cache-Control in response"
        assert "Expires" in headers, "There is no Expires in response"
