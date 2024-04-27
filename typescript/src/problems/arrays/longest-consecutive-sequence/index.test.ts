import { longestConsecutive } from "./index";

describe("longestConsecutive", () => {
    it("should return the length of the longest consecutive sequence", () => {
        expect(longestConsecutive([100, 4, 200, 1, 3, 2])).toBe(4);
        expect(longestConsecutive([0, 1, 2, 3, 4, 5])).toBe(6);
        expect(longestConsecutive([1, 2, 3, 4, 5, 6])).toBe(6);
        expect(longestConsecutive([9, 8, 7, 6, 5, 4])).toBe(6);
        expect(longestConsecutive([1])).toBe(1);
        expect(longestConsecutive([])).toBe(0);
    });
});
