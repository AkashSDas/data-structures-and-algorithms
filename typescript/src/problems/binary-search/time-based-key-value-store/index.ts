class TimeMap {
    private store: Record<string, [string, number][]>; // {key:[value,timestamp][]}

    constructor() {
        this.store = {};
    }

    set(key: string, value: string, timestamp: number): void {
        if (this.store[key]) {
            this.store[key].push([value, timestamp]);
        } else {
            this.store[key] = [[value, timestamp]];
        }
    }

    get(key: string, timestamp: number): string {
        const info = this.store[key];
        if (!info) return "";

        let start = 0;
        let end = info.length - 1;
        let result = "";

        while (start <= end) {
            const mid = start + Math.floor((end - start) / 2);
            const timestampAtMid = info[mid][1];

            if (timestampAtMid <= timestamp) {
                result = info[mid][0];
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return result;
    }
}
