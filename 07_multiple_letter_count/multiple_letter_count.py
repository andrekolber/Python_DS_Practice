def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    char_freq = {}

    for char in phrase:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    return char_freq