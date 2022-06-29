def end_zeros(number: int) -> int:
    if number == 0:
        return 1
    else:
        count = 0
        while True:
            if number % 10 != 0 or number == 0:
                break
            count = count + 1
            number = number / 10

        return count


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
