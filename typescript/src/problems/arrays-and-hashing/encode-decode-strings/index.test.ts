import { decode, encode } from "./index";

describe("Encoding and Decoding Functions", () => {
    test("Encode and decode a simple string array", () => {
        const input = ["Hello", "World"];
        const encoded = encode(input);
        const decoded = decode(encoded);

        expect(encoded).toBe("5:Hello5:World");
        expect(decoded).toEqual(input);
    });

    test("Encode and decode an empty string array", () => {
        const input: string[] = [];
        const encoded = encode(input);
        const decoded = decode(encoded);

        expect(encoded).toBe("");
        expect(decoded).toEqual(input);
    });

    test("Encode and decode a single-word string", () => {
        const input = ["OpenAI"];
        const encoded = encode(input);
        const decoded = decode(encoded);

        expect(encoded).toBe("6:OpenAI");
        expect(decoded).toEqual(input);
    });

    test("Encode and decode a single-character string", () => {
        const input = ["A"];
        const encoded = encode(input);
        const decoded = decode(encoded);

        expect(encoded).toBe("1:A");
        expect(decoded).toEqual(input);
    });

    // test("Decode with an invalid input returns an empty array", () => {
    //     const invalidInput = "InvalidInput";
    //     const decoded = decode(invalidInput);
    //     expect(decoded).toEqual([]);
    // });

    test("Encode and decode a large string array efficiently", () => {
        const largeInput = Array.from(
            { length: 1000 },
            (_, index) => `Word${index}`
        );
        const startTime = new Date().getTime();
        const encoded = encode(largeInput);
        const decoded = decode(encoded);
        const endTime = new Date().getTime();
        const elapsedTime = endTime - startTime;

        // Adjust the time threshold based on your performance expectations
        expect(elapsedTime).toBeLessThan(10); // Assuming it should complete within 10 milliseconds
        expect(decoded).toEqual(largeInput);
    });
});
