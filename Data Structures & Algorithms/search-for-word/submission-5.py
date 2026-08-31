class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, i, j):
                    return True
        return False;
    def search(self, board, word, i, j):
        print(i, j);
        if i > len(board) - 1 or i < 0 or j > len(board[0]) - 1 or j < 0: #ensures that i and j are with in range 
            return False;
        if word == board[i][j]: # defualt case
            return True;
        if board[i][j] != word[0]:
            return False;
        # Creates a new inner list for every row in the outer list
        temp = [row.copy() for row in board]
        temp[i][j] = "";
        return self.search(temp, word[1:], i, j + 1) or self.search(temp, word[1:], i, j - 1) or self.search(temp, word[1:], i + 1, j) or self.search(temp, word[1:], i - 1, j);


