def merge(intervals):
    # Step 1: Sort intervals by start
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        # If list empty → push
        if not merged:
            merged.append(interval)
        else:
            last = merged[-1]

            # ⭐ EXACT CONDITION YOU WANTED ⭐
            if interval[0] <= last[1]:
                # Overlap → merge
                last[1] = max(last[1], interval[1])
            else:
                # No overlap → new interval
                merged.append(interval)

    return merged


# Test
print(merge([[1,3],[2,6],[8,10],[15,18]]))
