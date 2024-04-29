/**
 * space complexity -- O(1)
 * time complexity -- O(n)
 */
function maxArea(height: number[]): number {
    let area = 0;
    let i = 0;
    let j = height.length - 1;

    while (i < j) {
        const heightAtI = height[i];
        const heightAtJ = height[j];
        const width = j - i;
        const minHeight = Math.min(heightAtI, heightAtJ);
        const newArea = minHeight * width;

        if (newArea > area) {
            area = newArea;
        }

        if (heightAtI > heightAtJ) {
            j--;
        } else {
            i++;
        }
    }

    return area;
}

/**
 * Time Limit Exceeded
 * space complexity -- O(1)
 * time complexity -- O(n^2)
 */
function maxArea2(height: number[]): number {
    let area = 0;

    for (let i = 0; i < height.length - 1; i++) {
        let j = height.length - 1;

        while (i < j) {
            const heightAtI = height[i];
            const heightAtJ = height[j];
            const width = j - i;
            const minHeight = Math.min(heightAtI, heightAtJ);
            const newArea = minHeight * width;
            if (newArea > area) {
                area = newArea;
            }

            j--;
        }
    }

    return area;
}
