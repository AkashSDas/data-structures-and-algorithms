function countMap(): Map<string, number> {
    const map = new Map<string, number>();
    for (let i = 97; i <= 122; i++) {
        map.set(String.fromCharCode(i), 0);
    }
    return map;
}

function checkInclusion(s1: string, s2: string): boolean {
    if (s1.length > s2.length) return false;

    const s1Count = countMap();
    const s2Count = countMap();

    for (let i = 0; i < s1.length; i++) {
        s1Count.set(s1[i], s1Count.get(s1[i])! + 1);
        s2Count.set(s2[i], s2Count.get(s2[i])! + 1);
    }

    let matches = 0;
    for (let char of s1Count.keys()) {
        if (s1Count.get(char) === s2Count.get(char)) {
            matches++;
        }
    }

    let left = 0;
    for (let right = s1.length; right < s2.length; right++) {
        if (matches === 26) return true;

        s2Count.set(s2[right], s2Count.get(s2[right])! + 1);
        if (s2Count.get(s2[right]) === s1Count.get(s2[right])) {
            matches++;
        } else if (s2Count.get(s2[right]) === s1Count.get(s2[right])! + 1) {
            matches--;
        }

        s2Count.set(s2[left], s2Count.get(s2[left])! - 1);
        if (s2Count.get(s2[left]) === s1Count.get(s2[left])) {
            matches++;
        } else if (s2Count.get(s2[left]) === s1Count.get(s2[left])! - 1) {
            matches--;
        }

        left++;
        console.log(matches, left, right);
    }

    if (matches === 26) return true;
    return false;
}

// console.log(checkInclusion("ab", "eidbaooo")); // true
