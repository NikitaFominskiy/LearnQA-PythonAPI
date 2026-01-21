from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("Get user details cases")
class TestUserGet(BaseCase):
    @allure.description("Попытка получить данные пользователя, будучи неавторизованным")
    def test_get_user_details_not_auth(self, record_property):
        # Метаданные для отчёта
        record_property("steps", "Попытка получить данные пользователя, будучи неавторизованным")
        record_property("expected", "В ответе только 'username' пользователя")

        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")


    @allure.description("Попытка получить данные своего пользователя (авторизованны этим пользователем)")
    def test_get_user_details_auth_as_same_user(self, record_property):
        # Метаданные для отчёта
        record_property("steps", "Попытка получить данные своего пользователя (авторизованны этим пользователем)")
        record_property("expected", "В ответе возвращаются поля 'username', 'email', 'firstName', 'lastName'")

        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)


    @allure.description("Попытка получить данные пользователя, будучи авторизованными другим пользователем")
    def test_get_user_details_auth_as_other_user(self, record_property):
        # Метаданные для отчёта
        record_property("steps", "Попытка получить данные пользователя, будучи авторизованными другим пользователем")
        record_property("expected", "В ответе только 'username' пользователя")

        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        other_user_id = user_id_from_auth_method + 1

        response2 = MyRequests.get(
            f"/user/{other_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["username"]
        Assertions.assert_json_has_keys(response2, expected_fields)
