import { groupAnagrams } from "./index";

describe("groupAnagrams", () => {
    it("should group anagrams together", () => {
        expect(
            groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        ).toEqual([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]);

        expect(groupAnagrams(["listen", "silent", "inlets", "tinsel"])).toEqual(
            [["listen", "silent", "inlets", "tinsel"]]
        );

        expect(groupAnagrams(["abc", "def", "ghi"])).toEqual([
            ["abc"],
            ["def"],
            ["ghi"],
        ]);
    });

    it("should return an empty array if input is empty", () => {
        expect(groupAnagrams([])).toEqual([]);
    });

    it("should return each string as a separate group if there are no anagrams", () => {
        expect(groupAnagrams(["hello", "world", "foo", "bar"])).toEqual([
            ["hello"],
            ["world"],
            ["foo"],
            ["bar"],
        ]);
    });
});
