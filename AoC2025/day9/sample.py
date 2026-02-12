from collections import deque
from bisect import bisect_right
import sys

def solve(red_lines):
    # Parse red tiles
    reds = []
    for line in red_lines:
        s = line.strip()
        if not s:
            continue
        r, c = map(int, s.split(","))
        reds.append((r, c))

    if not reds:
        return 0

    # bounding extremes
    min_r = min(r for r, _ in reds)
    max_r = max(r for r, _ in reds)
    min_c = min(c for _, c in reds)
    max_c = max(c for _, c in reds)

    # Build compression coordinates.
    # For each important coordinate v include v and v+1 so intervals [v, next-1] cover integer rows/cols.
    # Add outer padding so flood fill can start from outside.
    rows_set = set()
    cols_set = set()

    # include reds and reds+1
    for r, c in reds:
        rows_set.add(r)
        rows_set.add(r + 1)
        cols_set.add(c)
        cols_set.add(c + 1)

    # include global bounds and padding
    PAD = 1
    rows_set.add(min_r - PAD)
    rows_set.add(max_r + PAD + 1)  # +1 to make the top boundary exclusive
    cols_set.add(min_c - PAD)
    cols_set.add(max_c + PAD + 1)

    uniq_r = sorted(rows_set)
    uniq_c = sorted(cols_set)

    # Each compressed cell (i,j) represents original rows [uniq_r[i], uniq_r[i+1]-1]
    H = len(uniq_r) - 1
    W = len(uniq_c) - 1
    if H <= 0 or W <= 0:
        return 0

    # helpers: map an original coordinate x -> interval index i such that uniq[i] <= x <= uniq[i+1]-1
    def idx_r(x):
        i = bisect_right(uniq_r, x) - 1
        if i < 0: i = 0
        if i >= H: i = H - 1
        return i

    def idx_c(x):
        j = bisect_right(uniq_c, x) - 1
        if j < 0: j = 0
        if j >= W: j = W - 1
        return j

    # Represent wall tiles on interval grid
    red_cells = set()
    for r, c in reds:
        red_cells.add((idx_r(r), idx_c(c)))

    # Build green outline on interval grid by marking every interval cell that intersects each segment
    green_cells = set()
    N = len(reds)
    for i in range(N):
        r1, c1 = reds[i]
        r2, c2 = reds[(i + 1) % N]
        if r1 == r2:
            # horizontal segment at row r1, covers columns c_start..c_end inclusive
            r_idx = idx_r(r1)
            c_start, c_end = sorted((c1, c2))
            ci1 = idx_c(c_start)
            ci2 = idx_c(c_end)
            # Mark all interval columns whose intervals intersect [c_start, c_end]
            for ci in range(ci1, ci2 + 1):
                if (r_idx, ci) not in red_cells:
                    green_cells.add((r_idx, ci))
        elif c1 == c2:
            # vertical segment at col c1, covers rows r_start..r_end inclusive
            c_idx = idx_c(c1)
            r_start, r_end = sorted((r1, r2))
            ri1 = idx_r(r_start)
            ri2 = idx_r(r_end)
            for ri in range(ri1, ri2 + 1):
                if (ri, c_idx) not in red_cells:
                    green_cells.add((ri, c_idx))
        else:
            raise ValueError("Input must have axis-aligned consecutive red tiles (rows or cols equal).")

    # Flood fill OUTSIDE the loop on the interval grid
    outside = set()
    q = deque()
    # add boundary cells (all edge cells)
    for j in range(W):
        q.append((0, j))
        q.append((H - 1, j))
    for i in range(H):
        q.append((i, 0))
        q.append((i, W - 1))

    def is_wall_cell(ri, ci):
        return (ri, ci) in red_cells or (ri, ci) in green_cells

    while q:
        ri, ci = q.popleft()
        if (ri, ci) in outside:
            continue
        if is_wall_cell(ri, ci):
            continue
        outside.add((ri, ci))
        for dri, dci in ((1,0),(-1,0),(0,1),(0,-1)):
            nri, nci = ri + dri, ci + dci
            if 0 <= nri < H and 0 <= nci < W:
                q.append((nri, nci))

    # interior green cells = cells not outside and not wall
    inside_green_cells = set()
    for ri in range(H):
        for ci in range(W):
            if (ri, ci) in outside:
                continue
            if (ri, ci) in red_cells or (ri, ci) in green_cells:
                continue
            inside_green_cells.add((ri, ci))

    allowed_cells = red_cells | green_cells | inside_green_cells

    # Build block grid: 1 if forbidden (not allowed), 0 if allowed
    block = [[0]*W for _ in range(H)]
    for ri in range(H):
        for ci in range(W):
            if (ri, ci) not in allowed_cells:
                block[ri][ci] = 1

    # 2D prefix sum on block
    ps = [[0]*(W+1) for _ in range(H+1)]
    for i in range(H):
        row_sum = 0
        for j in range(W):
            row_sum += block[i][j]
            ps[i+1][j+1] = ps[i][j+1] + row_sum

    def rect_has_block(ri1, ci1, ri2, ci2):
        # inclusive indices
        return (ps[ri2+1][ci2+1] - ps[ri1][ci2+1] - ps[ri2+1][ci1] + ps[ri1][ci1]) > 0

    # Prepare mapping from original coordinate -> interval index for quick reuse
    # (we already have idx_r / idx_c functions)

    # Test all red pairs
    best = 0
    red_list = list(reds)
    R = len(red_list)
    for a in range(R):
        r1, c1 = red_list[a]
        for b in range(a+1, R):
            r2, c2 = red_list[b]
            # must be opposite corners -> different rows and different cols
            if r1 == r2 or c1 == c2:
                continue

            r_lo, r_hi = sorted((r1, r2))
            c_lo, c_hi = sorted((c1, c2))

            # map to interval indices (inclusive)
            ri1 = idx_r(r_lo)
            ri2 = idx_r(r_hi)
            ci1 = idx_c(c_lo)
            ci2 = idx_c(c_hi)

            if rect_has_block(ri1, ci1, ri2, ci2):
                continue

            # Inclusive tile count area
            area = (r_hi - r_lo + 1) * (c_hi - c_lo + 1)
            if area > best:
                best = area

    return best

if __name__ == "__main__":
    # read from file 'input' or stdin
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        with open(fname, 'r') as f:
            lines = f.readlines()
    else:
        try:
            with open('input', 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            # fallback: read stdin
            lines = sys.stdin.read().splitlines()

    result = solve(lines)
    print(result)
