import pytest
from main import filter_successful, group_and_sum


def test_filter_successful():
    data = [
        {"user_id": "u1", "amount": 10, "status": "SUCCESS"},
        {"user_id": "u1", "amount": 20, "status": "FAILED"}
    ]
    result = filter_successful(data)
    assert len(result) == 1
    assert result[0]['amount'] == 10


def test_group_and_sum():
    data = [
        {"user_id": "u1", "amount": 10, "status": "SUCCESS"},
        {"user_id": "u1", "amount": 20, "status": "SUCCESS"},
        {"user_id": "u2", "amount": 15, "status": "SUCCESS"},
    ]
    result = group_and_sum(data)
    assert result == {"u1": 30, "u2": 15}


def test_group_and_sum_empty():
    assert group_and_sum([]) == {}
