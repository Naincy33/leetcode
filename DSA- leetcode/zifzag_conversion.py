def convert(s: str, numRows: int) -> str:
    # edge case
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows
    curr = 0
    direction = 1  # 1 -> down, -1 -> up

    for c in s:
        rows[curr] += c
        
        # direction change
        if curr == 0:
            direction = 1
        elif curr == numRows - 1:
            direction = -1
        
        curr += direction

    return "".join(rows)


# Example
print(convert("PAYPALISHIRING", 3))
