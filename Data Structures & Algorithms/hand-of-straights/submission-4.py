
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique = sorted(set(hand))

        for num in unique:
            if count[num] > 0:
                freq = count[num]

                for i in range(groupSize):
                    if count[num + i] < freq:
                        return False

                    count[num + i] -= freq

        return True
