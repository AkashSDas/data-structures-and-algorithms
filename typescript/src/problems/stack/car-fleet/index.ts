type CarFleet = (target: number, position: number[], speed: number[]) => number;

const carFleet: CarFleet = (target, position, speed) => {
    // [position,speed][]
    const cars: [number, number][] = Array.from(position)
        .map(function (pos, idx): [number, number] {
            return [pos, speed[idx]];
        })
        .sort(function (a, b) {
            return a[0] - b[0]; // order based on position
        })
        .reverse();

    const fleetStack: number[] = []; // time to reach target

    for (let i = 0; i < cars.length; i++) {
        const car = cars[i];
        const timeToReachTarget = (target - car[0]) / car[1]; // distance diff / speed
        fleetStack.push(timeToReachTarget);
        const len = fleetStack.length;

        if (len >= 2 && fleetStack[len - 2] >= fleetStack[len - 1]) {
            fleetStack.pop();
        }
    }

    return fleetStack.length;
};
