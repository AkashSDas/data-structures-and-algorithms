class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows: dict[int, set[str]] = {}  # row_idx:elements_in_that_row
        cols: dict[int, set[str]] = {}
        boxes: dict[str, set[str]] = {}

        for row_idx, row in enumerate(board):
            row_elements = set()
            rows[row_idx] = row_elements

            for col_idx, col_item in enumerate(row):
                col_elements = cols.get(col_idx)

                if not col_elements:
                    col_elements = set()
                    cols[col_idx] = col_elements

                box_row_idx = row_idx // 3
                box_col_idx = col_idx // 3
                box_key = f"{box_row_idx}_{box_col_idx}"

                box_elements = boxes.get(box_key)

                if not box_elements:
                    box_elements = set()
                    boxes[box_key] = box_elements

                if col_item == ".":
                    continue

                exists_in_col = col_item in col_elements
                exists_in_row = col_item in row_elements
                exists_in_box = col_item in box_elements

                if any([exists_in_box, exists_in_col, exists_in_row]):
                    return False
                else:
                    col_elements.add(col_item)
                    row_elements.add(col_item)
                    box_elements.add(col_item)

        return True
