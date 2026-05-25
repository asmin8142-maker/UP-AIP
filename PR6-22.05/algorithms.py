# algorithms.py

"""
Реализации алгоритмов разной вычислительной сложности.
"""


# =========================
# O(1)
# =========================

def array_access(arr, index):
    """
    Time: O(1)
    Space: O(1)
    """
    return arr[index]


# =========================
# O(log n)
# =========================

def binary_search(arr, target):
    """
    Time: O(log n)
    Space: O(1)
    """

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# =========================
# O(n)
# =========================

def linear_search(arr, target):
    """
    Time: O(n)
    Space: O(1)
    """

    for i, value in enumerate(arr):

        if value == target:
            return i

    return -1


def sum_elements(arr):
    """
    Time: O(n)
    Space: O(1)
    """

    total = 0

    for value in arr:
        total += value

    return total


# =========================
# O(n log n)
# =========================

def merge_sort(arr):
    """
    Time: O(n log n)
    Space: O(n)
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# =========================
# O(n²)
# =========================

def bubble_sort(arr):
    """
    Time: O(n²)
    Space: O(1)
    """

    arr = arr.copy()

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if not swapped:
            break

    return arr


def insertion_sort(arr):
    """
    Time: O(n²)
    Space: O(1)
    """

    arr = arr.copy()

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


# =========================
# O(n³)
# =========================

def matrix_multiply(A, B):
    """
    Time: O(n³)
    Space: O(n²)
    """

    n = len(A)

    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):

        for j in range(n):

            for k in range(n):

                result[i][j] += A[i][k] * B[k][j]

    return result


# =========================
# O(2^n)
# =========================

def fibonacci(n):
    """
    Time: O(2^n)
    Space: O(n)
    """

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
