def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    print(shape, point)
    # steps = [(0, 0), ]
    # step_count = {(0, 0): 1}
    #
    # def add_step(x, y, p):
    #     try:
    #         step_count[(x, y)] += 2 * step_count[p]
    #     except KeyError:
    #         steps.append((x, y))
    #         step_count[(x, y)] = 2 * step_count[p]

    # while steps:
    #     steps.sort(key=lambda x: x[0])
    #     st = steps.pop(0)
    #     if st[0] + 1 < shape[0] and st[1] + 2 < shape[1]:
    #         add_step(st[0] + 1, st[1] + 2, (st[0], st[1]))
    #     if st[0] + 1 < shape[0] and st[1] - 2 >= 0:
    #         add_step(st[0] + 1, st[1] - 2, (st[0], st[1]))
    #     if st[0] + 2 < shape[0] and st[1] + 1 < shape[1]:
    #         add_step(st[0] + 2, st[1] + 1, (st[0], st[1]))
    #     if st[0] + 2 < shape[0] and st[1] - 1 >= 0:
    #         add_step(st[0] + 2, st[1] - 1, (st[0], st[1]))
    # return step_count[point]

    queue = [(0, 0), ]
    hesh = {(0, 0): 1}
    while queue:
        cell = queue.pop()
        if cell[0] + 1 < shape[0] and cell[1] + 2 < shape[1] and hesh.get((cell[0] + 1, cell[1] + 2)) is None:
            queue.append((cell[0] + 1, cell[1] + 2))
            hesh[(cell[0] + 1, cell[1] + 2)] = 0
        if cell[0] + 1 < shape[0] and cell[1] - 2 >= 0 and hesh.get((cell[0] + 1, cell[1] - 2)) is None:
            queue.append((cell[0] + 1, cell[1] - 2))
            hesh[(cell[0] + 1, cell[1] - 2)] = 0
        if cell[0] + 2 < shape[0] and cell[1] + 1 < shape[1] and hesh.get((cell[0] + 2, cell[1] + 1)) is None:
            queue.append((cell[0] + 2, cell[1] + 1))
            hesh[(cell[0] + 2, cell[1] + 1)] = 0
        if cell[0] + 2 < shape[0] and cell[1] - 1 >= 0 and hesh.get((cell[0] + 2, cell[1] - 1)) is None:
            queue.append((cell[0] + 2, cell[1] - 1))
            hesh[(cell[0] + 2, cell[1] - 1)] = 0

    my_steps = list(hesh.keys())
    my_steps.sort(key=lambda x: x[0])
    for cell in my_steps:
        if hesh.get((cell[0] + 1, cell[1] + 2)) is not None:
            hesh[(cell[0] + 1, cell[1] + 2)] += hesh[cell] * 2
        if hesh.get((cell[0] + 1, cell[1] - 2)) is not None:
            hesh[(cell[0] + 1, cell[1] - 2)] += hesh[cell] * 2
        if hesh.get((cell[0] + 2, cell[1] + 1)) is not None:
            hesh[(cell[0] + 2, cell[1] + 1)] += hesh[cell] * 2
        if hesh.get((cell[0] + 2, cell[1] - 1)) is not None:
            hesh[(cell[0] + 2, cell[1] - 1)] += hesh[cell] * 2

    return hesh[point]

if __name__ == '__main__':
    print(calculate_paths((8, 8), (7, 7)))
    print(calculate_paths((9, 9), (8, 8)))
