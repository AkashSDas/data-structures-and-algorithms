/**
 * time complexity -- O(n)
 * space complexity -- O(n)
 */
export function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) {
        return false;
    }

    const sChars: Record<string, number> = {};
    const tChars: Record<string, number> = {};

    for (let i = 0; i < s.length; i++) {
        sChars[s[i]] = (sChars[s[i]] ?? 0) + 1;
        tChars[t[i]] = (tChars[t[i]] ?? 0) + 1;
    }

    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (sChars[char] !== tChars[char]) {
            return false;
        }
    }

    return true;
}
