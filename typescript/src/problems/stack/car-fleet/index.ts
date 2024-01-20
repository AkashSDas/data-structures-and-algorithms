type CarFleet = (target: number, position: number[], speed: number[]) => number;

var carFleet: CarFleet = (target, position, speed) => {
    // [position,speed]
    var cars: [number, number][] = Array.from(position)
        .map(function (pos, idx): [number, number] {
            return [pos, speed[idx]];
        })
        .sort(function (a, b) {
            return a[0] - b[0]; // reverse order
        })
        .reverse();

    var fleetStack: number[] = []; // time to reach target

    for (let i = 0; i < cars.length; i++) {
        let car = cars[i];
        fleetStack.push((target - car[0]) / car[1]);
        let len = fleetStack.length;

        if (len >= 2 && fleetStack[len - 2] >= fleetStack[len - 1]) {
            fleetStack.pop();
        }
    }

    return fleetStack.length;
};

carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]);
