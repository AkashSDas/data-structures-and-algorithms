function groupAnagrams(strs: string[]): string[][] {
    var groups: Record<string, string[]> = {};

    for (let i = 0; i < strs.length; i++) {
        let str = strs[i];
        let counts = Array(26); // 26 chars a..z

        for (let j = 0; j < str.length; j++) {
            let ord = str.charCodeAt(j);

            if (counts[ord]) {
                counts[ord] += 1;
            } else {
                counts[ord] = 1;
            }
        }

        let key = counts.toString();
        if (groups[key]) {
            groups[key].push(str);
        } else {
            groups[key] = [str];
        }
    }

    return Object.values(groups);
}

function groupAnagrams2(strs: string[]): string[][] {
    var groups: Record<string, string[]> = {};

    for (let i = 0; i < strs.length; i++) {
        let sortedStr = strs[i].split("").sort().join("");
        let currentList = groups[sortedStr];

        if (currentList == undefined) {
            groups[sortedStr] = [strs[i]];
        } else {
            groups[sortedStr].push(strs[i]);
        }
    }

    return Object.values(groups);
}
