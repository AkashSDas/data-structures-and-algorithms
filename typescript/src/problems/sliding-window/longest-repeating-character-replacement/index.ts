function characterReplacement(s: string, k: number): number {
    const charCount: Record<string, number> = {};
    let maxLength = 0;
    let left = 0;
    let maxFrequency = 0;

    for (let right = 0; right < s.length; right++) {
        charCount[s[right]] = 1 + (charCount[s[right]] ?? 0);
        maxFrequency = Math.max(charCount[s[right]], maxFrequency); // don't need to update max frequence since we want the longest substring

        // length - frequence of the most frequent element <= k <-- condition for valid window
        while (right - left + 1 - maxFrequency > k) {
            charCount[s[left]]--;
            left++;
        }

        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
}

function characterReplacement1(s: string, k: number): number {
    const charCount: Record<string, number> = {};
    let maxLength = 0;
    let left = 0;

    for (let right = 0; right < s.length; right++) {
        charCount[s[right]] = 1 + (charCount[s[right]] ?? 0);

        // length - frequence of the most frequent element <= k <-- condition for valid window
        while (right - left + 1 - Math.max(...Object.values(charCount)) > k) {
            charCount[s[left]]--;
            left++;
        }

        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
}
