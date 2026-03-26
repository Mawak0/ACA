def segments_select(segments):
    def sort_f(a):
        return a[1]
    segments.sort(key=sort_f)
    right_max = -float("inf")
    answer = []
    for s in segments:
        if s[0] > right_max:
            right_max = s[1]
            answer.append(s)
    return answer

seg = [
    (0,5),
    (1,2),
    (2,5),
    (2,3),
    (5,8),
    (4,5),
    (4,8),
]

print(segments_select(seg))


def segments_select(segments, L, R):
    def sort_f(a):
        return a[0]

    segments.sort(key=sort_f)

    right_max = L
    answer = []
    i = 0
    n = len(segments)

    while right_max < R:
        best = right_max
        best_seg = None

        while i < n and segments[i][0] <= right_max:
            if segments[i][1] > best:
                best = segments[i][1]
                best_seg = segments[i]
            i += 1

        if best_seg is None:
            return None

        answer.append(best_seg)
        right_max = best

    return answer


seg = [
    (0, 5),
    (1, 2),
    (2, 5),
    (2, 3),
    (5, 8),
    (4, 5),
    (4, 8),
]

print(segments_select(seg, 0, 8))