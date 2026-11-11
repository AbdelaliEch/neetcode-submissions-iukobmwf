class Solution:
    def get_valid_neighbors(self, board, current_word_letter, current_pos, visited):
        neighbors = []
        if current_pos == (-1, -1):
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == current_word_letter:
                        neighbors.append((i, j))
        else:
            i, j = current_pos

            # right neighbor
            if j + 1 < len(board[0]) and board[i][j + 1] == current_word_letter and (i, j + 1) not in visited:
                neighbors.append((i, j + 1))
            
            # left neighbor
            if j - 1 >= 0 and board[i][j - 1] == current_word_letter and (i, j - 1) not in visited:
                neighbors.append((i, j - 1))
            
            # top neighbor
            if i - 1 >= 0 and board[i - 1][j] == current_word_letter and (i - 1, j) not in visited:
                neighbors.append((i - 1, j))
            
            # bottom neighbor
            if i + 1 < len(board) and board[i + 1][j] == current_word_letter and (i + 1, j) not in visited:
                neighbors.append((i + 1, j))
            
        return neighbors


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False

        def backtrack(letter_index, current_pos, visited):
            if letter_index == len(word) or self.found:
                self.found = True
                return

            valid_neighbors = self.get_valid_neighbors(board, word[letter_index], current_pos, visited)
            for neighbor in valid_neighbors:
                if self.found:
                    break
                i, j = neighbor
                visited.add(neighbor)
                backtrack(letter_index + 1, neighbor, visited)
                visited.remove(neighbor)

        backtrack(0, (-1, -1), set())
        return self.found
