function isValidSudoku(board: string[][]): boolean {
    var rows: Record<string, Set<string>> = {};
    var columns: Record<string, Set<string>> = {};
    var square: Record<string, Set<string>> = {}; // key - r/3_c/3

    for (let rowIdx = 0; rowIdx < 9; rowIdx++) {
        rows[rowIdx] = new Set<string>();

        for (let colIdx = 0; colIdx < 9; colIdx++) {
            if (columns[colIdx] == undefined) {
                columns[colIdx] = new Set<string>();
            }

            let squareRowIdx = Math.floor(rowIdx / 3);
            let squareColIdx = Math.floor(colIdx / 3);
            let key = `${squareRowIdx}_${squareColIdx}`;
            if (square[key] == undefined) {
                square[key] = new Set<string>();
            }

            let item = board[rowIdx][colIdx];

            if (item != ".") {
                if (
                    rows[rowIdx].has(item) ||
                    columns[colIdx].has(item) ||
                    square[key].has(item)
                ) {
                    return false;
                } else {
                    rows[rowIdx].add(item);
                    columns[colIdx].add(item);
                    square[key].add(item);
                }
            }
        }
    }
    return true;
}

console.log(
    isValidSudoku([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ])
);
