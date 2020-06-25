from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    print(stairway)
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
    step_2 = [stairway[0],]
    step_1 = [stairway[0] + stairway[1], stairway[1]]
    for i in range(2, len(stairway)):
        step_2, step_1 = step_1, list(map(lambda x: x + stairway[i], step_1 + step_2))
    return min(step_1)


if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]))
