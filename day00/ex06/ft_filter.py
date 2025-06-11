def ft_filter(func, iterable):
    """
    Custom implementation of filter() using list comprehension.
    Returns a list of elements for which func(x) is True.
    """
    if func is None:
        return [x for x in iterable if x]
    return [x for x in iterable if func(x)]
