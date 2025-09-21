from typing import List

def greet_all(names: List[str]) -> None:
    for name in names:
        print(f"Hello, {name}!")


def test_greet_testcse() -> None:
    names = ["Alice", "Bob", "Charlie"]
    greet_all(names)
    print("Test completed successfully.")
    print("This is a test message.")
    print("Another line added for testing.")


def number_to_string(num: int) -> str:
    return str(num)

def test_number_to_string() -> None:
    assert number_to_string(123) == "123"
    assert number_to_string(0) == "0"
    assert number_to_string(-456) == "-456"
    print("All tests passed for number_to_string.")
    print("testCase 2 passed.")



def add(a: int, b: int) -> int:
    return a + b

def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("All tests passed for add.")
    print("testCase 3 passed.")



if __name__ == "__main__":
    test_greet_testcse()
    test_number_to_string()
    test_add()