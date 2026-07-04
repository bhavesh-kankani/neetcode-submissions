class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.prefix_matrix = [[0 for _ in range(self.cols+1)] for _ in range(self.rows+1)]
        self.prefix_sum()
        return None

    def prefix_sum(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.prefix_matrix[i+1][j+1] = self.prefix_matrix[i+1][j] + self.matrix[i][j]
        # print(*self.prefix_matrix)
        for j in range(self.cols):
            for i in range(self.rows):
                if i == 1 and j == 1:
                    print(self.prefix_matrix[i+1][j+1])
                self.prefix_matrix[i+1][j+1] = self.prefix_matrix[i][j+1] + self.prefix_matrix[i+1][j+1]
                if i == 1 and j == 1:
                    print(self.prefix_matrix[i+1][j+1])
        # print(*self.prefix_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_matrix[row2+1][col2+1] - self.prefix_matrix[row1][col2+1] - self.prefix_matrix[row2+1][col1] + self.prefix_matrix[row1][col1]
