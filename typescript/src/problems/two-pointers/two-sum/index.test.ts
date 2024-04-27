import { twoSum } from "./index";

describe("twoSum", () => {
    it("should return the indices of two numbers that add up to the target", () => {
        expect(twoSum([2, 7, 11, 15], 9)).toEqual([1, 2]);
        expect(twoSum([2, 3, 4], 6)).toEqual([1, 3]);
    });

    it("should return [NaN, NaN] if no two numbers add up to the target", () => {
        expect(twoSum([1, 2, 3, 4], 10)).toEqual([NaN, NaN]);
        expect(twoSum([5, 6, 7], 8)).toEqual([NaN, NaN]);
    });
});
