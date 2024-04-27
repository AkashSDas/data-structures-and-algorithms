// Encode and decode a string. Don't maintain any state.
// Input - ["Hello", "World"]
// Output - ["Hello", "World"]
// Encode - "5:Hello5:World"

export function encode(text: string[]): string {
    let result = "";

    for (const word of text) {
        result += `${word.length}:${word}`;
    }

    return result;
}

export function decode(str: string): string[] {
    const result: string[] = [];

    for (let i = 0; i < str.length; i++) {
        let wordLength = "";

        while (str[i] !== ":") {
            wordLength += str[i];
            i++;
        }

        const wordLengthInt = parseInt(wordLength, 10);
        let word = "";

        for (let j = 0; j < wordLengthInt; j++) {
            i++;
            word += str[i];
        }

        result.push(word);
    }

    return result;
}
