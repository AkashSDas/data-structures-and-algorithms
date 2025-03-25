Triplet = list[int]


class Solution:
    def merge(self, triplet1: Triplet, triplet2: Triplet) -> Triplet:
        result: Triplet = []
        for i in range(3):
            result.append(max(triplet1[i], triplet2[i]))
        return result

    def mergeTriplets(self, triplets: list[Triplet], target: Triplet) -> bool:
        result: Triplet | None = None

        for triplet in triplets:
            if triplet == target:
                return True

            if all(triplet[i] <= target[i] for i in range(3)):
                if result:
                    result = self.merge(result, triplet)
                else:
                    result = triplet

            if target == result:
                return True

        return False
