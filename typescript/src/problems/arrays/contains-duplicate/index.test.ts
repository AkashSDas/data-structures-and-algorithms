import { containsDuplicate } from "./index";

describe("containsDuplicate", () => {
    it("returns true if there are duplicates in the array", () => {
        var nums = [1, 2, 3, 1];
        var result = containsDuplicate(nums);
        expect(result).toBe(true);
    });

    it("returns false if there are no duplicates in the array", () => {
        var nums = [1, 2, 3, 4];
        var result = containsDuplicate(nums);
        expect(result).toBe(false);
    });

    it("returns true for a large array with duplicates", () => {
        var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1];
        var result = containsDuplicate(nums);
        expect(result).toBe(true);
    });

    it("returns false for an empty array", () => {
        var nums: number[] = [];
        var result = containsDuplicate(nums);
        expect(result).toBe(false);
    });

    it("returns false for an array with a single number", () => {
        var nums = [1];
        var result = containsDuplicate(nums);
        expect(result).toBe(false);
    });
});
