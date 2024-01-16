export function isAnagram(s: string, t: string): boolean {
    if (s.length != t.length) {
        return false;
    }

    var sChars: Record<string, number> = {};
    var tChars: Record<string, number> = {};

    for (let i = 0; i < s.length; i++) {
        sChars[s[i]] = (sChars[s[i]] ?? 0) + 1;
        tChars[t[i]] = (tChars[t[i]] ?? 0) + 1;
    }

    for (let char in sChars) {
        let sCharLen = sChars[char];
        let tCharLen = tChars[char];

        if (tCharLen == undefined) {
            return false;
        }

        if (sCharLen != tCharLen) {
            return false;
        }
    }

    return true;
}

function isAnagram2(s: string, t: string): boolean {
    if (s.length != t.length) {
        return false;
    }

    var sChars: Record<string, number> = {};
    var tChars: Record<string, number> = {};

    for (let i = 0; i < s.length; i++) {
        sChars[s[i]] = (sChars[s[i]] ?? 0) + 1;
        tChars[t[i]] = (tChars[t[i]] ?? 0) + 1;
    }

    for (let char in sChars) {
        let sCharLen = sChars[char];
        let tCharLen = tChars[char];

        if (tCharLen == undefined) {
            return false;
        }

        if (sCharLen != tCharLen) {
            return false;
        }
    }

    return true;
}
