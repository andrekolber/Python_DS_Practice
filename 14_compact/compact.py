def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    non_true = ['', [], (),  False, None]
    return [ele for ele in lst if ele not in non_true]