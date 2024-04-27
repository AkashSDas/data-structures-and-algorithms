/**
 * time complexity -- O(1)
 * space complexity -- O(1)
 */
export function isAlphanumeric(char: string): boolean {
    const isNumber = !isNaN(parseFloat(char));
    const isAlphabet = char.toLowerCase() !== char.toUpperCase();
    return isNumber || isAlphabet;
}

/**
 * time complexity -- O(n)
 * space complexity -- O(n)
 */
export function clean(s: string): string {
    return s
        .split(" ")
        .filter((word) => isAlphanumeric(word))
        .map((word) => word.toLowerCase())
        .join("")
        .split("")
        .filter((char) => isAlphanumeric(char))
        .join("");
}

/**
 * time complexity -- O(n)
 * space complexity -- O(1)
 */
export function isPalindrome(s: string): boolean {
    const cleanStr = clean(s);
    let leftIdx = 0;
    let rightIdx = cleanStr.length - 1;

    while (leftIdx < rightIdx) {
        if (cleanStr[leftIdx] !== cleanStr[rightIdx]) {
            return false;
        }

        leftIdx++;
        rightIdx--;
    }

    return true;
}
