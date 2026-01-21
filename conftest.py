import pytest
import re

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Основной источник — self
        instance = item.funcargs.get("self") if hasattr(item, "funcargs") else None
        steps = getattr(instance, "steps", None)
        expected = getattr(instance, "expected", None)


        # Резервный источник — user_properties (если self нет или атрибуты не заданы)
        if steps is None:
            steps = next((prop[1] for prop in item.user_properties if prop[0] == "steps"), "Не указано")
        if expected is None:
            expected = next((prop[1] for prop in item.user_properties if prop[0] == "expected"), "Не указано")

        # Формируем отчёт
        actual = str(report.longrepr).split('AssertionError:')[-1].strip()
        if not actual:
            actual = str(report.longrepr)[-100:]  # последние 100 символов, если AssertionError не найден


        new_longrepr = (
            f"\n"
            f"Шаги: {steps}\n"
            f"Ожидаемый результат: {expected}\n"
            f"Действительный результат: AssertionError: {actual}"
        )
        report.longrepr = new_longrepr