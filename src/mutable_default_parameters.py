def append_to_list(value, lst=[]):
    """
    Appends a value to a list. If no list is provided, appends to a default list.

    WARNING: Using a mutable default parameter can lead to unexpected behavior.
    """
    lst.append(value)
    return lst


def append_to_list_fixed(value, lst=None):
    """
    Appends a value to a list. If no list is provided, creates a new list.

    This approach avoids the pitfalls of mutable default parameters.
    """
    if lst is None:
        lst = []
    lst.append(value)
    return lst


if __name__ == "__main__":
    print(append_to_list(1))  # Output: [1]
    print(append_to_list(2))  # Output: [1, 2]
    print(append_to_list(3, []))  # Output: [3]
    print(append_to_list(4))  # Output: [1, 2, 4] - unexpected behavior

    print(append_to_list_fixed(1))  # Output: [1]
    print(append_to_list_fixed(2))  # Output: [2]
    print(append_to_list_fixed(3, [1, 2]))  # Output: [1,2,3]
    print(append_to_list_fixed(4))  # Output: [4] - expected behavior
