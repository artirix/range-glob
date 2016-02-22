# coding=utf8

#  Split range to ranges that has its unique pattern.
#  Example for 12-345:
#
#  12- 19: 1[2-9]
#  20- 99: [2-9][0-9]
# 100-299: [1-2][0-9][0-9]
# 300-339: 3[0-3][0-9]
# 340-345: 34[0-5]

def glob_for_range(min_, max_):
    """
    > glob_for_range(12, 345)
    '{1[2-9],[2-9][0-9],[1-2][0-9][0-9],3[0-3][0-9],34[0-5]}'
    """
    subpatterns = split_to_patterns(min_, max_)    
    if len(subpatterns) > 1:
        return '{' + ','.join(subpatterns) + '}'
    else:
        return subpatterns[0]

def split_to_patterns(min_, max_):
    subpatterns = []

    start = min_
    for stop in split_to_ranges(min_, max_):
        subpatterns.append(range_to_pattern(start, stop))
        start = stop + 1

    return subpatterns


def split_to_ranges(min_, max_):
    stops = {max_}

    nines_count = 1
    stop = fill_by_nines(min_, nines_count)
    while min_ <= stop < max_:
        stops.add(stop)

        nines_count += 1
        stop = fill_by_nines(min_, nines_count)

    zeros_count = 1
    stop = fill_by_zeros(max_ + 1, zeros_count) - 1
    while min_ < stop <= max_:
        stops.add(stop)

        zeros_count += 1
        stop = fill_by_zeros(max_ + 1, zeros_count) - 1

    stops = list(stops)
    stops.sort()

    return stops


def fill_by_nines(integer, nines_count):
    return int(str(integer)[:-nines_count] + '9' * nines_count)


def fill_by_zeros(integer, zeros_count):
    return integer - integer % 10 ** zeros_count


def range_to_pattern(start, stop):
    pattern = ''
    any_digit_count = 0

    for start_digit, stop_digit in zip(str(start), str(stop)):
        if start_digit == stop_digit:
            pattern += start_digit
        elif start_digit != '0' or stop_digit != '9':
            pattern += '[{}-{}]'.format(start_digit, stop_digit)
        else:
            any_digit_count += 1

    pattern = pattern + '[0-9]' * any_digit_count
    return pattern
