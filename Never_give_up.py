def is_valid_parentheses(
    s,
):
    stack = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    if not s:
        return True
    for x in s:
        if x in (
            "(",
            "{",
            "[",
        ):
            stack.append(x)
        elif x in pairs:
            if not stack:
                return False
        last = stack.pop()
        if pairs[x] != last:
            return False
    return len(stack) == 0


def bubble_sort(
    arr,
):
    """Sorts a list in ascending order using bubble sort. O(n²) time complexity."""
    if not isinstance(
        arr,
        list,
    ):
        raise TypeError("Input must be a list")
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                (
                    arr[j],
                    arr[j + 1],
                ) = (
                    arr[j + 1],
                    arr[j],
                )
                swapped = True
        if not swapped:
            break
    return arr


def binary_search(
    arr,
    target,
):
    if not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        raise ValueError("Array must be sorted")
    """Массив должен быть отсортирован!!!"""
    if not arr:
        return -1
    if not isinstance(
        arr,
        list,
    ):
        raise TypeError("Input must be a list")
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        """Чтобы не переполнить массив если оч большой"""
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


import requests


def get_user_data(
    user_id,
):
    if not isinstance(
        user_id,
        int,
    ):
        raise TypeError("User_id must be an integer")
    if user_id < 0:
        raise ValueError("Number can not be negative")
    URL = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(URL, timeout=5)
    except requests.RequestException:
        raise ValueError("Network Error")
    if response.status_code != 200:
        raise ValueError("User not found")
    data = response.json()
    return {
        "name": data["name"],
        "email": data["email"],
    }



import sqlite3
def get_high_earners(min_salary):
    """Fetch employees with salary above min_salary from employees.db."""
    if not isinstance(min_salary, (int, float)):
        raise TypeError("min_salary must be an int or float")
    if min_salary <= 0:
        raise ValueError("Number cannot be negative")
    try:
        conn = sqlite3.connect("employees.db")
    except sqlite3.Error:
        raise ValueError("Database error")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
    )''')
    conn.commit()
    cursor.execute('''INSERT OR IGNORE INTO employees VALUES(?, ?, ?, ?)''',
                   (1, "Alice", "IT", 60000))
    cursor.execute('''INSERT OR IGNORE INTO employees VALUES(?, ?, ?, ?)''',
                   (2, "Bob", "HR", 70000))
    conn.commit()
    cursor.execute('SELECT name, salary FROM employees WHERE salary > min_salary')
    result = cursor.fetchall()
    conn.close()



