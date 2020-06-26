from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    # print(stairway)
    # length = 0
    # i = 0
    # while i < len(stairway):
    #     if len(stairway) - i == 1:
    #         length += stairway[i]
    #         break
    #     if stairway[i] < stairway[i+1]:
    #         length += stairway[i]
    #         i += 1
    #     else:
    #         length += stairway[i+1]
    #         i += 2
    # return length

    # step_2 = [stairway[0],]
    # step_1 = [stairway[0] + stairway[1], stairway[1]]
    # for i in range(2, len(stairway)):
    #     step_2, step_1 = step_1, list(map(lambda x: x + stairway[i], step_1 + step_2))
    # return min(step_1)


    if len(stairway) == 0:
        return 0
    return stairway[-1] + min(stairway_path(stairway[:-1]), stairway_path(stairway[:-2]))


if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]))
    # print(stairway_path([4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2]))
    # print(stairway_path([5, 11, 43, 2, 23, 43, 22, 12, 6, 8]))
    # print(stairway_path([4, 12, 32, 22, 1, 7, 0, 12, 4, 2, 2]))
