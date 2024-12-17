from main import next_board_state


def compare_state(expected_state, actual_state):
    if expected_state == actual_state:
        print("Passed 1")
    else:
        print("FAILED 1!")
        print("Expected: ")
        print(expected_state)
        print("Actual: ")
        print(actual_state)


if __name__ == "__main__":
    # TEST : #1 dead cells with no live neighbors
    init_state1 = [
        [
            0,
            0,
            0,
        ],
        [
            0,
            0,
            0,
        ],
        [
            0,
            0,
            0,
        ],
    ]
    expected_next_state1 = [
        [
            0,
            0,
            0,
        ],
        [
            0,
            0,
            0,
        ],
        [
            0,
            0,
            0,
        ],
    ]

    actual_next_state1 = next_board_state(init_state1)
    compare_state(expected_next_state1, actual_next_state1)

    # TEST : #2 dead cells with no live neighbors
    init_state2 = [
        [
            0,
            0,
            1,
        ],
        [
            0,
            1,
            1,
        ],
        [
            0,
            0,
            0,
        ],
    ]
    expected_next_state2 = [
        [
            0,
            1,
            1,
        ],
        [
            0,
            1,
            1,
        ],
        [
            0,
            0,
            0,
        ],
    ]

    actual_next_state2 = next_board_state(init_state2)
    compare_state(expected_next_state2, actual_next_state2)
