class Board:
    players = ('X', 'O')

    def __init__(self, size=3):
        self.size = size
        self.__create()
    
    def __create(self):
        self.board = []
        for _ in range(self.size):
            self.board.append([None] * self.size)
    
    def __getPlayer(self, marker):
        for i in range(len(self.players)):
            if self.players[i] == marker:
                return i + 1
        
        return None

    def __getIndex(self, position):
        position = int(position)

        if position < 1 or position > (self.size * self.size):
            return None, None

        remainder = position % self.size

        row = position // self.size
        if remainder == 0: row -= 1

        col = remainder - 1
        if remainder == 0: col = self.size - 1

        return row, col

    def reset(self):
        self.__create()
    
    def registerPlayerMarkers(self, p1='X', p2='O'):
        self.players = (p1, p2)
    
    def update(self, position, player):
        try:
            player = int(player)
            position  = int(position)
        except ValueError:
            return False

        if player < 1 and player > 2:
            return False
        
        row, col = self.__getIndex(position)

        if row is None or col is None:
            return False

        if self.board[row][col] is not None:
            return False

        self.board[row][col] = self.players[player - 1]

        return True
            
    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                value = self.board[i][j]
                if value is None:
                    value = " "

                if j == 0:
                    print(" {} ".format(value), end="")
                else:
                    print("| {} ".format(value), end="")
            print("")
            if i < (self.size - 1):
                print("____" * self.size)
    
    def winner(self):
        # Horizantal
        for i in range(self.size):
            markers = set()
            for j in range(self.size):
                markers.add(self.board[i][j])
            markers = list(markers)
            if len(markers) == 1 and markers[0] is not None:
                return self.__getPlayer(markers[0])

        # Vertical
        for i in range(self.size):
            markers = set()
            for j in range(self.size):
                markers.add(self.board[j][i])
            markers = list(markers)
            if len(markers) == 1 and markers[0] is not None:
                return self.__getPlayer(markers[0])

        # Diagonal
        markers = set()
        for i in range(self.size):
            markers.add(self.board[i][i])
        markers = list(markers)
        if len(markers) == 1 and markers[0] is not None:
            return self.__getPlayer(markers[0])
        
        # Diagonal
        markers = set()
        i = 0
        j = self.size - 1
        while i < self.size and j >= 0:
            markers.add(self.board[i][j])
            i += 1
            j -= 1
        markers = list(markers)
        if len(markers) == 1 and markers[0] is not None:
            return self.__getPlayer(markers[0])
        
        return None

    def tie(self):
        for row in self.board:
            for col in row:
                if col is None:
                    return False
        
        return True
        

