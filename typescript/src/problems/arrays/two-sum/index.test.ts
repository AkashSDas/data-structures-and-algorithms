import { twoSum } from "./";

describe("twoSum", () => {
    it("should return the indices of two numbers that add up to the target", () => {
        expect(twoSum([2, 7, 11, 15], 9).sort()).toEqual([0, 1]);
        expect(twoSum([3, 2, 4], 6).sort()).toEqual([1, 2]);
        expect(twoSum([3, 3], 6).sort()).toEqual([0, 1]);
    });

    it("should return [NaN, NaN] if no two numbers add up to the target", () => {
        expect(twoSum([1, 2, 3, 4], 10)).toEqual([NaN, NaN]);
        expect(twoSum([], 5)).toEqual([NaN, NaN]);
    });
});
