def bumpy1(sequence):
    lengths = [1 for _ in sequence]
    signs = [0 for _ in sequence]

    for i, num in enumerate(sequence):
        for j in range(i):
            if signs[j] == 0:
                # this means there's only a single number, and hence
                # it can go either way
                if num > sequence[j]:
                    lengths[i] = lengths[j] + 1
                    signs[i] = 1
                elif num < sequence[j]:
                    lengths[i] = lengths[j] + 1
                    signs[i] = -1

            if signs[j] == 1 and num < sequence[j]:
                if lengths[i] <= lengths[j]:
                    lengths[i] = lengths[j] + 1
                    signs[i] = -1

            if signs[j] == -1 and num > sequence[j]:
                if lengths[i] <= lengths[j]:
                    lengths[i] = lengths[j] + 1
                    signs[i] = 1

    return max(lengths)


def bumpy2(sequence):
    max_length = 1
    sign = 0
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            continue
        if sign == 0:
            max_length += 1
            if sequence[i] > sequence[i - 1]:
                sign = 1
            elif sequence[i] < sequence[i - 1]:
                sign = -1
        if sign == 1:
            if sequence[i] < sequence[i - 1]:
                max_length += 1
                sign = -1
        if sign == -1:
            if sequence[i] > sequence[i - 1]:
                max_length += 1
                sign = 1

    return max_length


def bumpy3(sequence):
    max_length = [0 for _ in sequence]
    sign = [0 for _ in sequence]
    max_length[0] = 1

    for i in range(1, len(sequence)):
        if sign[i-1] == 0:
            if sequence[i] == sequence[i - 1]:
                sign[i] = sign[i-1]
                max_length[i] = max_length[i-1]

            if sequence[i] > sequence[i - 1]:
                sign[i] = +1
                max_length[i] = max_length[i-1] + 1

            if sequence[i] < sequence[i - 1]:
                sign[i] = -1
                max_length[i] = max_length[i-1] + 1

        if sign[i-1] == 1:
            if sequence[i] < sequence[i - 1]:
                sign[i] = -sign[i-1]
                max_length[i] = max_length[i-1] + 1
            else:
                sign[i] = sign[i-1]
                max_length[i] = max_length[i-1]

        if sign[i-1] == -1:
            if sequence[i] > sequence[i - 1]:
                sign[i] = -sign[i-1]
                max_length[i] = max_length[i-1] + 1
            else:
                sign[i] = sign[i-1]
                max_length[i] = max_length[i-1]

    return max_length[-1]


bumpy = bumpy3


def main():
    cases = [
        {"input": [2, 4, -1, 9, 0, 5, -2], "expected": 7},
        {"input": [2, 4, 7, 3, 10, 5, 5], "expected": 5},
        {"input": [1, 2, 0, 7, 3, 5, 4], "expected": 7},
        {"input": [3, 3, 4, 4], "expected": 2},
        {"input": [1, 2, 0, 7, 3, 5], "expected": 6},
        {"input": [1, 2, 0, 0, 3, 5, 3, 6, 6, 0], "expected": 7},
        {"input": [1, 2], "expected": 2},
        {"input": [2, 4, 4, 4, 4, -1, 9, 0, 5, -2], "expected": 7},
        {"input": [2, 4, 7, 3, 10, 5, -5], "expected": 5},
        {"input": [5, 5, -1, 2, 2, 3, 4], "expected": 3},
        {"input": [-1, 5, -1, 5, 5, 5, -1, 1, -
                   1, 1, -1, 1, -1, 1], "expected": 12},
        {"input": [5, 5, -1, 2, 2, 3, 4, 1], "expected": 4},
        {"input": [5], "expected": 1},
        {"input": [5, 5], "expected": 1},
        {"input": [5, 5, 5, 5, 5, 5], "expected": 1},
    ]

    for case in cases:
        A = case["input"]
        expected = case["expected"]
        result = bumpy(A)
        if result != expected:
            print(f"❌ expected: {expected}, got: {result} for {A}")
        else:
            print(f"✅ {A} has expected result: {result}")


if __name__ == "__main__":
    main()
    # print(bumpy([2, 4, 7, 3, 10, 5, 5]))
