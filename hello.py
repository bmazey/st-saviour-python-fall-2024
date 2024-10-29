def least(numbers: list[int]) -> int:
    small = 100
    for number in numbers:
        if number < small:
            small = number
    return small

