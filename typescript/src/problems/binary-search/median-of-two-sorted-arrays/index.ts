function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    let A = nums1;
    let B = nums2;

    if (nums1.length > nums2.length) {
        A = nums2; // A is the smaller array
        B = nums1;
    }

    let left = 0;
    let right = A.length;

    while (true) {
        const midA = Math.floor((left + right) / 2);
    }
}
