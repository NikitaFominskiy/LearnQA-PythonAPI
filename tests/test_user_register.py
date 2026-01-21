import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("Registration cases")
class TestUserRegister(BaseCase):

    @allure.description("Попытка создать пользователя (позитивный)")
    def test_create_user_successfully(self, record_property):
        # Метаданные для отчёта
        record_property("steps", "Попытка создать пользователя (позитивный)")
        record_property("expected", "В ответе возвращается ID созданного пользователя")

        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Попытка создать пользователя с существующим в системе email")
    def test_create_user_with_existing_email(self, record_property):
        # Метаданные для отчёта
        record_property("steps", "Попытка создать пользователя с существующим в системе email")
        record_property("expected", "Статус 400, email уже занят")

        email='vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.description("Попытка создать пользователя с некорректным email - без символа @")
    def test_create_user_with_invalid_email(self, record_property):
        # Метаданные для отчёта
        record_property("steps", "Попытка создать пользователя с некорректным email - без символа @")
        record_property("expected", "Статус 400, email без символа @")

        data = self.prepare_registration_wrong_email()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"


    @pytest.mark.parametrize("missing_field", [
        "username",
        "firstName",
        "lastName",
        "email",
        "password"
    ])
    @allure.description("Попытка создать пользователя без указания одного из полей")
    def test_create_user_with_missing_field(self, missing_field, record_property):
        # Метаданные для отчёта
        record_property("steps", "Попытка создать пользователя без указания одного из полей")
        record_property("expected", "Статус 400, отсутствие любого параметра не дает зарегистрировать пользователя")

        data = self.prepare_registration_data()
        data.pop(missing_field)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {missing_field}", f"Unexpected response content {response.content}"


    @allure.description("Попытка создать пользователя с очень коротким именем в один символ")
    def test_create_user_with_short_firstname(self, record_property):
        # Метаданные для отчёта
        record_property("steps", "Попытка создать пользователя с очень коротким именем в один символ")
        record_property("expected", "Статус 400, Имя слишком короткое")

        data = self.prepare_registration_with_short_firstname()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too short", f"Unexpected response content {response.content}"


    @allure.description("Попытка создать пользователя с очень длинным именем - длиннее 250 символов")
    def test_create_user_with_long_firstname(self, record_property):
        # Метаданные для отчёта
        record_property("steps", "Попытка создать пользователя с очень длинным именем - длиннее 250 символов")
        record_property("expected", "Статус 400, Имя слишком длинное")

        data = self.prepare_registration_with_long_firstname()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long", f"Unexpected response content {response.content}"