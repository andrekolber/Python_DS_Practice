def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    result = ''
    list_of_words = phrase.split()
    for word in list_of_words:
        result += word.capitalize() + " "

    return result.strip()