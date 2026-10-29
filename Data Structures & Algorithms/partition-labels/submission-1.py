class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}

        # Store first and last occurrence
        for i, ch in enumerate(s):
            if ch not in intervals:
                intervals[ch] = [i, i]
            else:
                intervals[ch][1] = i

        # Sort intervals by starting index
        arr = sorted(intervals.values())

        res = []

        start, end = arr[0]

        for i in range(1, len(arr)):
            next_start, next_end = arr[i]

            # Overlapping interval
            if next_start < end:
                end = max(end, next_end)

            # Separate partition
            else:
                res.append(end - start + 1)
                start, end = next_start, next_end

        # Last partition
        res.append(end - start + 1)

        return res