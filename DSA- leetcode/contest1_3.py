def solve(n, A, T):
    # ---------------- PART 1: Closest Pair Sum -----------------
    arr = sorted(A)
    l, r = 0, n - 1
    best_diff = float('inf')
    best_sums = []

    # Find all pairs with closest sum
    while l < r:
        s = arr[l] + arr[r]
        d = abs(s - T)

        if d < best_diff:
            best_diff = d
            best_sums = [(arr[l], arr[r])]
        elif d == best_diff:
            best_sums.append((arr[l], arr[r]))

        if s < T:
            l += 1
        else:
            r -= 1

    # Allow both directions (x,y) and (y,x)
    target_pairs = set()
    for x, y in best_sums:
        target_pairs.add((x, y))
        target_pairs.add((y, x))

    # Find the first such pair in original array order
    best_pair = None
    for i in range(n):
        for j in range(i + 1, n):
            if (A[i], A[j]) in target_pairs:
                if abs(A[i] + A[j] - T) == best_diff:
                    best_pair = (A[i], A[j])
                    break
        if best_pair:
            break

    print(best_pair[0], best_pair[1])

    # ---------------- PART 2: Interval Scheduling -----------------
    intervals = []
    for i in range(0, n, 2):
        intervals.append((A[i], A[i + 1]))

    intervals.sort(key=lambda x: x[1])  # Sort by end time

    count = 0
    last_end = -10**30

    for s, f in intervals:
        if s >= last_end:
            count += 1
            last_end = f

    print(count)


# ---------------- RUN IN VS CODE -----------------
if __name__ == "__main__":
    # Example input (VS Code me manually enter karoge)
    # n = 6
    # A = [1 4 2 3 7 5]
    # T = 8

    n = int(input("Enter n: ").strip())
    A = list(map(int, input("Enter array: ").split()))
    T = int(input("Enter target: ").strip())

    solve(n, A, T)


