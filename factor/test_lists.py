import lists

def test_summation():
    first = [0, 1, 2, 3, 4]
    assert lists.summation(first) == 10

    second = [-1, 0, -3, 1]
    assert lists.summation(second) == -3

def test_find_negative():
    first = [0, 1, 2, -3, 4]
    assert lists.find_negative(first) == 3

    second = [-1, 0, 0, 0]
    assert lists.find_negative(second) == 0

def test_remove():
    n = 0
    first = [0, 1, 1, 0, 0, 1]
    result = lists.remove(first, n)

    assert result[0] == 1
    assert result[1] == 1
    assert result[2] == 1
    assert len(result) == 3

    n = 2
    second = [1, 1, 1, 2, 2]
    result = lists.remove(second, n)

    assert result[0] == 1
    assert result[1] == 1
    assert result[2] == 1
    assert len(result) == 3

def test_merge():
    first = [0, 2, 4, 8]
    second = [1, 3, 5, 9]

    result = lists.merge(first, second)
    assert result[0] == 0
    assert result[1] == 1
    assert result[2] == 2
    assert result[3] == 3
    assert result[4] == 4
    assert result[5] == 5
    assert result[6] == 8
    assert result[7] == 9
    assert len(result) == 8

def test_round_up():
    first = [0.5, 1.2, 4.3, 7.8]
    result = lists.round_up(first)

    assert result[0] == 1
    assert result[1] == 1
    assert result[2] == 4
    assert result[3] == 8
    assert len(result) == 4

def test_evens_only():
    first = [1, 2, 4, 7, 8, 3]
    result = lists.evens_only(first)

    assert result[0] == 2
    assert result[1] == 4
    assert result[2] == 8
    assert len(result) == 3

    second = [12, -14, 0, 7, 11]
    result = lists.evens_only(second)

    assert result[0] == 12
    assert result[1] == -14
    assert result[2] == 0
    assert len(result) == 3

def test_last_of_four_digits():
    first = [1004, 7888, 5632, 9810]
    result = lists.last_of_four_digits(first)

    assert result[0] == 4
    assert result[1] == 8
    assert result[2] == 2
    assert result[3] == 0
    assert len(result) == 4

    second = [1017, 7844, 5646, 9000]
    result = lists.last_of_four_digits(second)

    assert result[0] == 7
    assert result[1] == 4
    assert result[2] == 6
    assert result[3] == 0
    assert len(result) == 4
