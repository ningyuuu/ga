def missing(sequence):
    """Find the missing number in a sequence of numbers."""
    gap = sequence[1] - sequence[0]
    return missing_recursive(sequence, gap, 0, len(sequence) - 1)


def missing_recursive(sequence, gap, start, end):
    if start == end:
        return

    if start == end - 1:
        if sequence[end] == sequence[start] + gap:
            return
        else:
            return sequence[start] + gap

    seq_gap = sequence[end] - sequence[start]
    if seq_gap == gap * (end - start):
        return

    mid = (start + end) // 2

    return missing_recursive(sequence, gap, start, mid) or missing_recursive(sequence, gap, mid, end)


print(missing([1, 2, 4]))

tests = [
    ([1, 3, 5, 9, 11], 7),
    ([2, 6, 10, 14, 18, 22, 30], 26),
    ([-10, -6, -2, 2, 6, 14], 10),
    ([1000, 2000, 3000, 5000, 6000], 4000),
    ([1, 2, 4, 5, 6, 7], 3),
    ([100, 300, 500, 700, 1100], 900),
    ([1, 2, 4], 3),
    ([-3, 0, 3, 9, 12], 6),
    ([10, 20, 30, 50, 60], 40),
    ([10, 20, 30, 40, 60], 50),
    ([-2, 0, 2, 6, 8], 4),
    (list(range(0, 10000, 2)) + [10002, 10004], 10000),
    ([20, 17, 14, 8, 5, 2], 11),
    ([1, 2, 4, 5, 6], 3),
    ([2147483647 - 6, 2147483647 - 4, 2147483647 - 2, 2147483647 + 2], 2147483647),
    (list(range(100)) + list(range(101, 200)), 100),
    # ([1, 2, 3, 4, 6], 3)
]

for test in tests:
    seq, ans = test
    assert missing(seq) == ans
