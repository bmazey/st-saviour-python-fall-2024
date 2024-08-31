from shredder import shred_first_character, shred_last_character


def test_shredder():
    # ensure first character is removed
    assert shred_first_character('st. saviour') == 't. saviour'
    assert shred_first_character('pandas') == 'andas'
    assert shred_first_character('s') == ''

    # ensure last character is removed
    assert shred_last_character('st. saviour') == 'st. saviou'
    assert shred_last_character('pandas') == 'panda'
    assert shred_last_character('s') == ''

    # both functions should return an empty string when given an empty string
    assert shred_first_character('') == ''
    assert shred_last_character('') == ''