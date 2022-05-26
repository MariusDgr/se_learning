from re import I


def is_number_valid(arr):
    dot_count = 0
    for i, char in enumerate(arr):
        if char == ".":
            dot_count += 1

            if i == 0 or i == (len(arr) - 1) or dot_count > 1:
                return False
    return True

if __name__ == "__main__":

    arr = [("4.325", True),
            ("1.1.1", False),
            ("222", True),
            ("22.", False),
            ("0.1", True),
            ("22.22.", False),]
    
    for test in arr:
        res = is_number_valid(test[0]) == test[1]
        if not res:
            print(f"Test {test[0]} failed")






