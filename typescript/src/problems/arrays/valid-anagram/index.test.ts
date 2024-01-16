import { isAnagram } from "./index";

describe("isAnagram", () => {
    it("should return true for valid anagrams", () => {
        expect(isAnagram("anagram", "nagaram")).toBe(true);
        expect(isAnagram("listen", "silent")).toBe(true);
        expect(isAnagram("heart", "earth")).toBe(true);
    });

    it("should return false for invalid anagrams", () => {
        expect(isAnagram("listen", "silence")).toBe(false);
        expect(isAnagram("heart", "earthly")).toBe(false);
    });

    it("should return false for strings with different lengths", () => {
        expect(isAnagram("anagram", "anagrams")).toBe(false);
        expect(isAnagram("listen", "list")).toBe(false);
        expect(isAnagram("heart", "hearts")).toBe(false);
    });
});
