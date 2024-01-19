// Encode and decode a string. Don't maintain any state.
// Input - ["Hello", "World"]
// Output - ["Hello", "World"]
// Encode - "5:Hello5:World"

export function encode(str: string[]): string {
    var result = "";

    for (let word of str) {
        result += word.length + ":" + word;
    }

    return result;
}

console.log(encode(["James", "Bond"])); // 5:James4:Bond

export function decode(str: string): string[] {
    var result: string[] = [];

    for (let i = 0; i < str.length; i++) {
        let length = "";

        while (str[i] !== ":") {
            length += str[i];
            i++;
        }

        let wordLength = parseInt(length);
        let word = "";

        for (let j = 0; j < wordLength; j++) {
            i++;
            word += str[i];
        }

        result.push(word);
    }

    return result;
}

console.log(decode("5:James4:Bond")); // ["James", "Bond"]
