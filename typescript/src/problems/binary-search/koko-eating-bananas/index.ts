function minEatingSpeed(piles: number[], h: number): number {
    let start = 1;
    let end = Math.max(...piles);
    let result = end;

    while (start <= end) {
        const mid = start + Math.floor((end - start) / 2);

        let hrs = 0;
        for (const pile of piles) {
            hrs += Math.ceil(pile / mid);
        }

        if (hrs <= h) {
            result = mid;
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    return result;
}
