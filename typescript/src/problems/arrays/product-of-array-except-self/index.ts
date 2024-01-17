function productExceptSelf(nums: number[]): number[] {
    var output = Array(nums.length);

    var prefix = 1;
    for (let i = 0; i < nums.length; i++) {
        if (i == 0) {
            output[i] = 1;
        } else {
            output[i] = prefix;
        }

        prefix = prefix * nums[i];
    }

    var postfix = 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        if (i == nums.length - 1) {
            output[i] = output[i];
        } else {
            output[i] = postfix * output[i];
        }

        postfix = postfix * nums[i];
    }

    return output;
}

console.log(productExceptSelf([2, 3, 4, 5]));
