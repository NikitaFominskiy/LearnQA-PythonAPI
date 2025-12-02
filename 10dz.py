import pytest


def test_input_length():
    user_input = input("Set a phrase: ")

    assert len(user_input) < 15, f"Phrase have more then {len(user_input)} symbols"



