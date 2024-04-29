import { threeSum } from "./index";

describe("threeSum", () => {
    it("should return an array of triplets that sum to zero", () => {
        // Test case 1
        expect(threeSum([-1, 0, 1, 2, -1, -4])).toEqual([
            [-1, -1, 2],
            [-1, 0, 1],
        ]);

        // Test case 2
        expect(threeSum([0, 0, 0, 0])).toEqual([[0, 0, 0]]);

        // Test case 3
        expect(threeSum([-2, 0, 1, 1, 2])).toEqual([
            [-2, 0, 2],
            [-2, 1, 1],
        ]);
    });

    it("should return an empty array if no triplets sum to zero", () => {
        // Test case 4
        expect(threeSum([1, 2, 3, 4, 5])).toEqual([]);

        // Test case 5
        expect(threeSum([-1, -2, -3, -4, -5])).toEqual([]);
    });
});
