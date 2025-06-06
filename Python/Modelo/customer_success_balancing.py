import time
import pytest

def customer_success_balancing(customer_success, customers, customer_success_away):
    # ===============================================
    # =========== Write your solution here ==========
    # ===============================================
    pass


def build_size_entities(size, score):
    """Helper function to build entities with same score"""
    result = []
    for i in range(size):
        result.append({"id": i + 1, "score": score})
    return result

def map_entities(arr):
    """Helper function to map array to entities"""
    return [{"id": index + 1, "score": item} for index, item in enumerate(arr)]

def array_seq(count, start_at):
    """Helper function to create sequential array"""
    return list(range(start_at, start_at + count))


def test_scenario_1():
    css = [
        {"id": 1, "score": 60},
        {"id": 2, "score": 20},
        {"id": 3, "score": 95},
        {"id": 4, "score": 75},
    ]
    customers = [
        {"id": 1, "score": 90},
        {"id": 2, "score": 20},
        {"id": 3, "score": 70},
        {"id": 4, "score": 40},
        {"id": 5, "score": 60},
        {"id": 6, "score": 10},
    ]
    cs_away = [2, 4]
    
    assert customer_success_balancing(css, customers, cs_away) == 1

def test_scenario_2():
    css = map_entities([11, 21, 31, 3, 4, 5])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away = []
    
    assert customer_success_balancing(css, customers, cs_away) == 0

def test_scenario_3():
    test_timeout_ms = 100
    test_start_time = time.time() * 1000
    
    css = map_entities(array_seq(999, 1))
    customers = build_size_entities(10000, 998)
    cs_away = [999]
    
    result = customer_success_balancing(css, customers, cs_away)
    assert result == 998
    
    elapsed_time = (time.time() * 1000) - test_start_time
    if elapsed_time > test_timeout_ms:
        raise Exception(f"Test took longer than {test_timeout_ms}ms!")

def test_scenario_4():
    css = map_entities([1, 2, 3, 4, 5, 6])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away = []
    
    assert customer_success_balancing(css, customers, cs_away) == 0

def test_scenario_5():
    css = map_entities([100, 2, 3, 6, 4, 5])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away = []
    
    assert customer_success_balancing(css, customers, cs_away) == 1

def test_scenario_6():
    css = map_entities([100, 99, 88, 3, 4, 5])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away = [1, 3, 2]
    
    assert customer_success_balancing(css, customers, cs_away) == 0

def test_scenario_7():
    css = map_entities([100, 99, 88, 3, 4, 5])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away = [4, 5, 6]
    
    assert customer_success_balancing(css, customers, cs_away) == 3

def test_scenario_8():
    css = map_entities([60, 40, 95, 75])
    customers = map_entities([90, 70, 20, 40, 60, 10])
    cs_away = [2, 4]
    
    assert customer_success_balancing(css, customers, cs_away) == 1
