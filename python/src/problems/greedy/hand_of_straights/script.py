from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # If total cards can't be divided into equal groups, return False
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)  # Frequency of each card
        hand.sort()  # Sort to ensure consecutive groups

        for card in hand:
            if count[card] == 0:
                continue  # If card is already used, skip it

            # Try forming a consecutive group
            for i in range(groupSize):
                if count[card + i] == 0:
                    return False  # Can't form a full group
                count[card + i] -= 1  # Use this card from count

        return True
