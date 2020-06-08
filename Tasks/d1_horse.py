def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    print(shape, point)
    steps = [(0, 0), ]
    step_count = {(0, 0): 1}
    while steps:
        steps.sort()
        st = steps.pop(0)
        if st[0] + 1 < shape[0] and st[1] + 2 < shape[1]:
            if (st[0] + 1, st[1] + 2) not in steps:
                steps.append((st[0] + 1, st[1] + 2))
                step_count[(st[0] + 1, st[1] + 2)] = 2 * step_count[(st[0], st[1])]
            else:
                step_count[(st[0] + 1, st[1] + 2)] += 2 * step_count[(st[0], st[1])]
        if st[0] + 1 < shape[0] and st[1] - 2 >= 0:
            if (st[0] + 1, st[1] - 2) not in steps:
                steps.append((st[0] + 1, st[1] - 2))
                step_count[(st[0] + 1, st[1] - 2)] = 2 * step_count[(st[0], st[1])]
            else:
                step_count[(st[0] + 1, st[1] - 2)] += 2 * step_count[(st[0], st[1])]
        if st[0] + 2 < shape[0] and st[1] + 1 < shape[1]:
            if (st[0] + 2, st[1] + 1) not in steps:
                steps.append((st[0] + 2, st[1] + 1))
                step_count[(st[0] + 2, st[1] + 1)] = 2 * step_count[(st[0], st[1])]
            else:
                step_count[(st[0] + 2, st[1] + 1)] += 2 * step_count[(st[0], st[1])]
        if st[0] + 2 < shape[0] and st[1] - 1 >= 0:
            if (st[0] + 2, st[1] - 1) not in steps:
                steps.append((st[0] + 2, st[1] - 1))
                step_count[(st[0] + 2, st[1] - 1)] = 2 * step_count[(st[0], st[1])]
            else:
                step_count[(st[0] + 2, st[1] - 1)] += 2 * step_count[(st[0], st[1])]
    # print(step_count)
    return step_count[point]


if __name__ == '__main__':
    print(calculate_paths((8, 8), (7, 7)))
    print(calculate_paths((9, 9), (8, 8)))
