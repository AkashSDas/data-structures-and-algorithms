import { topKFrequent } from "./index";

describe("topKFrequent", () => {
    it("should return the top k frequent elements", () => {
        expect(topKFrequent([1, 1, 1, 2, 2, 3], 2)).toEqual([1, 2]);
        expect(topKFrequent([1, 1, 1, 2, 2, 3], 3)).toEqual([1, 2, 3]);
        expect(topKFrequent([1, 1, 1, 2, 2, 3], 1)).toEqual([1]);
        expect(topKFrequent([1, 2, 3, 4, 5], 3)).toEqual([1, 2, 3]);
        expect(topKFrequent([1, 2, 3, 4, 5], 5)).toEqual([1, 2, 3, 4, 5]);
    });

    it("should return an empty array when k is 0", () => {
        expect(topKFrequent([1, 2, 3, 4, 5], 0)).toEqual([]);
    });

    it("should handle empty input array", () => {
        expect(topKFrequent([], 3)).toEqual([]);
    });
});
