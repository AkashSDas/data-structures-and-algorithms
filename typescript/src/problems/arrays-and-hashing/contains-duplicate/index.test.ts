import { containsDuplicate } from "./index";

describe("containsDuplicate", () => {
    it("returns true if there are duplicates in the array", () => {
        const nums = [1, 2, 3, 1];
        const result = containsDuplicate(nums);
        expect(result).toBe(true);
    });

    it("returns false if there are no duplicates in the array", () => {
        const nums = [1, 2, 3, 4];
        const result = containsDuplicate(nums);
        expect(result).toBe(false);
    });

    it("returns true for a large array with duplicates", () => {
        const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1];
        const result = containsDuplicate(nums);
        expect(result).toBe(true);
    });

    it("returns false for an empty array", () => {
        const nums: number[] = [];
        const result = containsDuplicate(nums);
        expect(result).toBe(false);
    });

    it("returns false for an array with a single number", () => {
        const nums = [1];
        const result = containsDuplicate(nums);
        expect(result).toBe(false);
    });
});
