function maxProfit(prices: number[]): number {
    let left = 0; // buy
    let right = 0; // sell
    let profit = 0;

    while (right < prices.length) {
        if (prices[left] < prices[right]) {
            profit = Math.max(profit, prices[right] - prices[left]);
        } else {
            left = right; // new minimum, min past price
        }

        right++;
    }

    return profit;
}

function maxProfit2(prices: number[]): number {
    let prevMin = prices[0];
    let profit = 0;

    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < prevMin) {
            prevMin = prices[i];
        }

        if (prices[i] - prevMin > profit) {
            profit = prices[i] - prevMin;
        }
    }

    return profit;
}

function maxProfit1(prices: number[]): number {
    let profit = 0;

    for (let i = 0; i < prices.length; i++) {
        for (let j = i + 1; j < prices.length; j++) {
            if (prices[i] < prices[j] && prices[j] - prices[i] > profit) {
                profit = prices[j] - prices[i];
            }
        }
    }

    return profit;
}
