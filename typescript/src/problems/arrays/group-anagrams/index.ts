/**
 * time complexity - O(n*m) (n -- length of strs, m -- length of str)
 * space complexity - O(n)
 */
export function groupAnagrams(strs: string[]): string[][] {
    const groups: Record<string, string[]> = {};

    for (let i = 0; i < strs.length; i++) {
        const str = strs[i];
        const counts = Array(26); // a..z

        for (let j = 0; j < str.length; j++) {
            const ord = str.charCodeAt(j);

            if (counts[ord]) {
                counts[ord] += 1;
            } else {
                counts[ord] = 1;
            }
        }

        const key = counts.toString();
        if (groups[key]) {
            groups[key].push(str);
        } else {
            groups[key] = [str];
        }
    }

    return Object.values(groups);
}

/**
 * time complexity - O(n*klogk) (n -- length of strs, k -- length of str in case of sorting)
 * space complexity - O(n)
 */
export function groupAnagrams2(strs: string[]): string[][] {
    const groups: Record<string, string[]> = {};

    for (let i = 0; i < strs.length; i++) {
        const str = strs[i];
        const key = str.split("").sort().join("");

        if (groups[key]) {
            groups[key].push(str);
        } else {
            groups[key] = [str];
        }
    }

    return Object.values(groups);
}
