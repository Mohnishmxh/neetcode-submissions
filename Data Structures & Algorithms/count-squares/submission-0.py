from collections import defaultdict

class CountSquares:

    def __init__(self):
        # Maps (x, y) -> frequency of occurrences
        self.point_counts = defaultdict(int)
        # Tracks unique points to iterate efficiently
        self.points = []

    def add(self, point: list[int]) -> None:
        p = tuple(point)
        if self.point_counts[p] == 0:
            self.points.append(p)
        self.point_counts[p] += 1

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        total_squares = 0

        # Test each recorded point (x2, y2) as a diagonal opposite
        for x2, y2 in self.points:
            side = abs(x1 - x2)
            # Must satisfy: side > 0 and |x1 - x2| == |y1 - y2|
            if side == 0 or side != abs(y1 - y2):
                continue

            # The two remaining corners must be (x1, y2) and (x2, y1)
            cnt_diag = self.point_counts[(x2, y2)]
            cnt_v1   = self.point_counts[(x1, y2)]
            cnt_v2   = self.point_counts[(x2, y1)]

            total_squares += cnt_diag * cnt_v1 * cnt_v2

        return total_squares