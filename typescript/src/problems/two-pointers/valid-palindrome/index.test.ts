import { clean } from "./index";

describe("clean", () => {
    it("should remove non-alphanumeric characters and convert to lowercase", () => {
        expect(clean("A man, a plan, a canal: Panama")).toEqual(
            "amanaplanacanalpanama"
        );
        expect(clean("race a car")).toEqual("raceacar");
        expect(clean("1234")).toEqual("1234");
        expect(clean("")).toEqual("");
    });
});
