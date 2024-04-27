import { productExceptSelf } from "./index";

describe("productExceptSelf", () => {
    it("should return the product of array except self", () => {
        expect(productExceptSelf([1, 2, 3, 4])).toEqual([24, 12, 8, 6]);
        expect(productExceptSelf([0, 1, 2, 3])).toEqual([6, 0, 0, 0]);
        expect(productExceptSelf([-1, -2, -3, -4])).toEqual([-24, -12, -8, -6]);
        expect(productExceptSelf([5])).toEqual([5]);
    });
});
