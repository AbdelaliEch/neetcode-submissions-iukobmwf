class Solution:
    def freePlacesAfterAddingQueen(self, current_free_places, n, x, y):
        captured_places = set()
        remaining_free_places = set()

        for i in range(n):
            captured_places.add((x, i))
            captured_places.add((i, y))
            
            if 0 <= x + i < n and 0 <= y + i < n:
                captured_places.add((x + i, y + i))
            
            if 0 <= x - i < n and 0 <= y - i < n:
                captured_places.add((x - i, y - i))

            if 0 <= x - i < n and 0 <= y + i < n:
                captured_places.add((x - i, y + i))

            if 0 <= x + i < n and 0 <= y - i < n:
                captured_places.add((x + i, y - i))
        
        for pos in current_free_places:
            if pos not in captured_places:
                remaining_free_places.add(pos)
        
        return remaining_free_places


    def solveNQueens(self, n: int) -> List[List[str]]:
        outputCoordinates = []

        def dfs(row, current_queens_positions, current_free_places):
            if row == n:
                outputCoordinates.append(current_queens_positions.copy())
                return

            if not current_free_places:
                return

            for column in range(n):
                if (row, column) not in current_free_places:
                    continue

                current_queens_positions.append((row, column))
                new_free_places = self.freePlacesAfterAddingQueen(current_free_places, n, row, column)
                dfs(row + 1, current_queens_positions, new_free_places)
                current_queens_positions.pop()
            
        current_queens_positions = []
        current_free_places = {(i, j) for i in range(n) for j in range(n)}
        for column in range(n):
            current_queens_positions.append((0, column))
            new_free_places = self.freePlacesAfterAddingQueen(current_free_places, n, 0, column)
            dfs(1, current_queens_positions, new_free_places)
            current_queens_positions.pop()


        return [["." * j + "Q" + "." * (len(coord) - j - 1) for _, j in coord] for coord in outputCoordinates]



# print(self.queenCapturedPlaces(current_free_places, 4, 0, 0))


# if a queen in i, j
# that means it takes the whole row i (horizontal), the whole column j (vertical), and diagonally (i + 1 , j + 1), (i - 1 , j - 1),...


# what if we track the free places so far instead of comparing each time

# before adding any queen, we will check if its position is in a free place, if yes, add it , if no invalid

# then if we add it, we need to update the current free places





