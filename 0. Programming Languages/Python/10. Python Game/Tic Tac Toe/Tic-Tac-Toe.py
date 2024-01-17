import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple
import math

class AI:
    def __init__(self, player):
        self.player = player


    def get_move(self, game):
        best_move = None
        best_score = -math.inf

        for move in game.get_valid_moves():
            game.make_move(move)
            score = self.minimax(game, self.player.value, 4, -math.inf, math.inf)  # Pass player's value
            game.undo()

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, game, player, depth, alpha, beta):
        
        if depth == 0 or game.is_game_over():
            return self.evaluate(game)

        if player == self.player.value:
            max_score = -math.inf

            for move in game.get_valid_moves():
                game.make_move(move)
                score = self.minimax(game, -player, depth-1, alpha, beta)
                game.undo()
                max_score = max(score, max_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score

        else:
            min_score = math.inf

            for move in game.get_valid_moves():
                game.make_move(move)
                score = self.minimax(game, -player, depth-1, alpha, beta)
                game.undo()
                min_score = min(score, min_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score

    def evaluate(self, game):
        if game.has_winner():
            return 1
        elif game.has_winner() == False:
            return -1
        else:
            return 0

class Player(NamedTuple):
    label: str
    color: str
    value: int


class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 30 * 27  # 30 rows, 27 columns
DEFAULT_PLAYERS = (
    Player(label = "X", color = "black", value = 1),
    Player(label = "O", color = "red", value = -1),
)

ai = AI(DEFAULT_PLAYERS[1])

print(ai)

class Game:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = [[Move(row, col) for col in range(self.board_size)] for row in range(self.board_size)]
        self._has_winner = False
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        winning_combos = []

        # Rows and columns
        for row in range(self.board_size - 3):
            for col in range(self.board_size):
                winning_combos.append([(row + i, col) for i in range(4)])

        for row in range(self.board_size):
            for col in range(self.board_size - 3):
                winning_combos.append([(row, col + i) for i in range(4)])

        # Diagonals
        for row in range(self.board_size - 3):
            for col in range(self.board_size - 3):
                winning_combos.append([(row + i, col + i) for i in range(4)])

                if col >= 3:
                    winning_combos.append([(row + i, col - i) for i in range(4)])

        return winning_combos

    def _is_valid_move(self, move):
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    def _process_move(self, move):
        if self._is_valid_move(move):
            self._current_moves[move.row][move.col] = move
            self._check_for_winner()
            if not self._has_winner:
                self.current_player = next(self._players)

    def _check_for_winner(self):
        for combo in self._winning_combos:
            combo_labels = [self._current_moves[row][col].label for row, col in combo]
            if len(set(combo_labels)) == 1 and combo_labels[0] != "":
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        return self._has_winner

    def _is_tied(self):
        no_winner = not self._has_winner
        all_moves_played = all(move.label != "" for row in self._current_moves for move in row)
        return no_winner and all_moves_played

    def _toggle_player(self):
        self.current_player = next(self._players)
    
    # Function for AI
    def get_valid_moves(self):
        return [move for row in self._current_moves for move in row if move.label == ""]
    
    def make_move(self, move):
        self._current_moves[move.row][move.col] = move
        self._check_for_winner()
        if not self._has_winner:
            self.current_player = next(self._players)
            
    def undo(self):
        self._has_winner = False
        self.current_player = next(self._players)
        self._current_moves = [[Move(row, col) for col in range(self.board_size)] for row in range(self.board_size)]
        
    def is_game_over(self):
        return self._is_tied() or self.has_winner()


class Board(tk.Tk):
    def __init__(self, game=Game()):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._ai_play = False
        self._create_board_grid()
        self._create_board_bindings()

    def _create_menu(self):
        menu_bar = tk.Menu(master = self)
        self.config(menu = menu_bar)
        game_menu = tk.Menu(menu_bar, tearoff=0)
        game_menu.add_command(label = "Restart", command = self._restart_game)
        game_menu.add_command(label="AI Play", command=self._toggle_ai_play) 
        game_menu.add_separator()
        game_menu.add_command(label = "Quit", command = self.destroy)
        menu_bar.add_cascade(label = "Game", menu = game_menu)
        
    def _toggle_ai_play(self):
        self._ai_play = not self._ai_play

    def _create_board_display(self):
        display_frame = tk.Frame(master = self)
        display_frame.pack(fill = tk.X)
        self.display = tk.Label(
            master = display_frame,
            text = "Get ready?",
            font = font.Font(size = 15, weight = "bold"),
        )
        self.display.pack()

    def _create_board_grid(self):
        canvas_frame = tk.Frame(master = self)
        canvas_frame.pack(fill = tk.BOTH, side = tk.LEFT, expand=True)
        self.canvas = tk.Canvas(
            master = canvas_frame,
            width = 1920,
            height = 1080,
            bg = "white",
        )
        for row in range(40):
            self.canvas.create_line(0, row * 30, 1920, row * 30, fill = "black")
        for col in range(64):
            self.canvas.create_line(col * 30, 0, col * 30, 1080, fill = "black")
        self.canvas.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

    def _create_board_bindings(self):
        self.canvas.bind("<Button-1>", self._play)

    def _restart_game(self):
        self._game = Game()
        self._ai_play = False
        self._clear_board()
        self._update_display()

    def _clear_board(self):
        self.canvas.delete("all")
        for row in range(40):
            self.canvas.create_line(0, row * 30, 1920, row * 30, fill="black")
        for col in range(64):
            self.canvas.create_line(col * 30, 0, col * 30, 1080, fill="black")

    def _update_display(self):
        if self._game.has_winner():
            self.display.config(text = f"{self._game.current_player.label} wins!") 
        elif self._game._is_tied():
            self.display.config(text = "Tie!")
        else:
            if self._ai_play and self._game.current_player == ai.player:
                self.display.config(text="AI's turn")
            else:  
                self.display.config(text=f"{self._game.current_player.label}'s turn")

    def _highlight_cells(self):
        for row, col in self._game.winner_combo:
            x = col * 30 + 15
            y = row * 30 + 15
            self.canvas.create_line(x - 15, y - 15, x + 15, y + 15, fill="green", width=3)

    def _play(self, event):
        if self._ai_play and self._game.current_player == ai.player:
            # AI turn
            move = ai.get_move(self._game)
            self._update_board(move)
            self._game._process_move(move)
        else:
            # Human turn
            col = event.x // 30
            row = event.y // 30
            move = Move(row, col, self._game.current_player.label)
            self._update_board(move)
            self._game._process_move(move)
        self._update_display()
        if self._game.has_winner():
            self._highlight_cells()
        elif self._game._is_tied():
            self._display_tie_message()
        else:
            self._update_display()

    def _update_board(self, move):
        row, col = move.row, move.col
        x = col * 30 + 15
        y = row * 30 + 15
        self.canvas.create_text(
            x,
            y,
            text=move.label,
            font=font.Font(size = 20, weight = "bold"),
            fill=self._game.current_player.color,
        )


def main():
    """Create the game's board and run its main loop."""
    board = Board()
    board.mainloop()


if __name__ == "__main__":
    main()