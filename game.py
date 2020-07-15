import random


class XoGame:
    def __init__(self, players):
        self.game_board = [" "] * 9
        self.game_over = False
        self.x_player = players[0]
        self.o_player = players[1]
        self.result = None

    def print_board(self):
        '''Print the game board.'''
        print("---------")
        print("| " + self.game_board[0] + " " + self.game_board[1] + " " + self.game_board[2] + " |")
        print("| " + self.game_board[3] + " " + self.game_board[4] + " " + self.game_board[5] + " |")
        print("| " + self.game_board[6] + " " + self.game_board[7] + " " + self.game_board[8] + " |")
        print("---------")

    def check_winner(self):
        '''Check to see if there has been a winner.'''
        # Initialise x and o counts
        x_count = self.game_board.count("X")
        o_count = self.game_board.count("O")

        # Check win states
        # Horizontal win
        top_row = self.game_board[0] == self.game_board[1] == self.game_board[2] and self.game_board[0] in "XO"
        mid_row = self.game_board[3] == self.game_board[4] == self.game_board[5] and self.game_board[3] in "XO"
        bot_row = self.game_board[6] == self.game_board[7] == self.game_board[8] and self.game_board[6] in "XO"

        # Vertical win
        left_col = self.game_board[0] == self.game_board[3] == self.game_board[6] and self.game_board[0] in "XO"
        mid_col = self.game_board[1] == self.game_board[4] == self.game_board[7] and self.game_board[1] in "XO"
        right_col = self.game_board[2] == self.game_board[5] == self.game_board[8] and self.game_board[2] in "XO"

        # Diagonal win
        diag_one = self.game_board[0] == self.game_board[4] == self.game_board[8] and self.game_board[0] in "XO"
        diag_two = self.game_board[6] == self.game_board[4] == self.game_board[2] and self.game_board[6] in "XO"

        # Win states along with winner: [winning combo, winner]
        win_states = [[top_row, self.game_board[0]],
                      [mid_row, self.game_board[3]],
                      [bot_row, self.game_board[6]],
                      [left_col, self.game_board[0]],
                      [mid_col, self.game_board[1]],
                      [right_col, self.game_board[2]],
                      [diag_one, self.game_board[0]],
                      [diag_two, self.game_board[6]]]

        win_count = 0
        # Check for multiple wins
        for i in range(8):
            if win_states[i][0]:
                win_count += 1

        # If only one winning config, determine winner
        if win_count == 1:
            win_idx = [i[0] for i in win_states]
            win_idx = win_idx.index(True)
            winner = win_states[win_idx][1]

            self.game_over = True
            self.result = winner
            print("{} wins!".format(self.result))

        # Set game state to impossible if more than one winning config.
        elif win_count > 1 and all(x == winner[0] for x in self.result):
            self.result = "Impossible"
            self.game_over = True

        # Set game state to impossible if one player is too many moves ahead.
        elif abs(x_count - o_count) >= 2:
            self.result = "Impossible"
            self.game_over = True

        else:
            self.game_over = False

        # Set game not finished, still possible moves
        if not self.game_over and ("_" in self.game_board or " " in self.game_board):
            self.result = "Game not finished"
            self.game_over = False

        # Game board full, no winner - Draw
        elif ("_" not in self.game_board or " " not in self.game_board) and not self.game_over:
            self.result = "Draw"
            self.game_over = True

    def check_two(self):
        # Check if AI or opponent is one move away from winning. Return pos. of winning position if true, else
        # return random move
        pass

    def ai_move(self, letter, difficulty):
        '''Let the computer (AI) make a move'''
        print('Making move level "{}"'.format(difficulty))
        free_spaces = []

        # Determine which board locations are free
        for i, j in enumerate(self.game_board):
            if j == "_" or j == " ":
                free_spaces.append(i)

        if difficulty == "easy":
            # Select random free space
            ai_move = random.choice(free_spaces)
        elif difficulty == "medium":
            # ---- TO DO ----
            ai_move = random.choice(free_spaces)
        elif difficulty == "hard":
            # ---- TO DO ----
            ai_move = random.choice(free_spaces)

        # Mark game board with the AI's letter
        self.game_board[ai_move] = letter
        self.print_board()

    def user_move(self, letter):
        ''' Allow the user to make a move.'''
        while True:
            user_move = input("Enter the coordinates:")

            move_coord1, move_coord2 = user_move.split()

            # Map coordinates to game_board
            board_mapping = {"1 3": 0, "2 3": 1, "3 3": 2,
                             "1 2": 3, "2 2": 4, "3 2": 5,
                             "1 1": 6, "2 1": 7, "3 1": 8}

            # Check only contains numbers
            if user_move.lower().islower():
                print("You should enter numbers!")

            # Check coordinate range
            elif (not 1 <= int(move_coord1) <= 3) or (not 1 <= int(move_coord2) <= 3):
                print("Coordinates should be from 1 to 3!")

            # Check if an empty position was selected
            elif self.game_board[board_mapping[user_move]] == "X" or self.game_board[board_mapping[user_move]] == "O":
                print("This cell is occupied! Choose another one!")

            else:
                self.game_board[board_mapping[user_move]] = letter
                self.print_board()
                return

    def run(self):
        '''Start game.'''
        self.print_board()

        while not self.game_over:
            # Play X move
            if self.x_player == "user":
                self.user_move("X")
            elif self.x_player == "easy" or self.o_player == "medium" or self.x_player == "hard":
                self.ai_move("X", self.x_player)

            # Check if there's been a winner
            self.check_winner()
            if self.game_over:
                return

            # Play O move
            if self.o_player == "user":
                self.user_move("O")
            elif self.o_player == "easy" or self.o_player == "medium" or self.o_player == "hard":
                self.ai_move("O", self.o_player)

            # Check if there's been a winner
            self.check_winner()


if __name__ == "__main__":

    game_start = False

    # Specify valid input
    valid_users = ["user", "easy", "medium", "hard"]

    while True:
        start_command = input()
        if " " in start_command:
            start_command = start_command.split(" ")

            if start_command[0] == "start":
                game_start = True

                game_players = start_command[1:3]
                if game_players[0] in valid_users and game_players[1] in valid_users:
                    break

                else:
                    print("Bad parameters!")

        elif start_command == "exit":
            game_start = False
            break

    if game_start:
        xo_game = XoGame(game_players)
        xo_game.run()
