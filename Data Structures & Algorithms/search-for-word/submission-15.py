class Solution:
    def get_valid_neighbors(self, board, current_word_letter, current_pos, visited):
        neighbors = []
        i, j = current_pos
        if j + 1 < len(board[0]) and board[i][j + 1] == current_word_letter and (i, j + 1) not in visited:
            neighbors.append((i, j + 1))
        
        if j - 1 >= 0 and board[i][j - 1] == current_word_letter and (i, j - 1) not in visited:
            neighbors.append((i, j - 1))
        
        if i - 1 >= 0 and board[i - 1][j] == current_word_letter and (i - 1, j) not in visited:
            neighbors.append((i - 1, j))
        
        if i + 1 < len(board) and board[i + 1][j] == current_word_letter and (i + 1, j) not in visited:
            neighbors.append((i + 1, j))
            
        return neighbors


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        self.visited = set()

        def backtrack(letter_index, current_pos):
            if letter_index == len(word) or self.found:
                self.found = True
                return

            valid_neighbors = self.get_valid_neighbors(board, word[letter_index], current_pos, self.visited)
            for neighbor in valid_neighbors:
                if self.found:
                    break
                i, j = neighbor
                self.visited.add(neighbor)
                backtrack(letter_index + 1, neighbor)
                self.visited.remove(neighbor)

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == word[0]:
                    self.visited.add((i, j))
                    backtrack(1, (i, j))
                    self.visited.remove((i, j))
                    if self.found:
                        break
        
        return self.found
