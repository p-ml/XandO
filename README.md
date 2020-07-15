
# Xs And Os

Xs and Os game (Tic-Tac-Toe) with options for 2-player local play, or single player vs. 3 levels of computer AI.

## INSTRUCTIONS
Run game.py
The 'Ready to play?' prompt will appear in the terminal. Three   parameters are required to begin the game:
*[start/exit] [x-player] [o-player]*

The first positional command, start/exit, is self-explanatory. Exit will terminate the game, and start will allow the game to begin.

The *[x-player]* and *[o-player]* options specify who is playing as each letter (user or computer). There are three levels of AI difficulty. The input options are:
- 'user' - indicates a human is playing.
- 'easy' - indicates the computer AI is playing with easy difficulty.
- 'medium' - indicates the computer AI is playing with medium difficulty.
- 'hard' - indicates the computer AI is playing with hard difficulty.

For example, to start the game with a human playing as 'X' and an easy computer AI playing as 'O', the 'Ready to play?' command would be:

> start user easy

Or to watch two medium difficulty AI battle it out:
> start medium medium

--------
Currently, the 'easy' AI difficulty is the only one properly implemented. This option means that the AI will select a move at random, with no real strategy.

## TO-DO
### Medium Difficulty
The medium difficulty will make a move with the following  process:
1.  If it can win in one move (if it has two in a row), it places a third to get three in a row and win.
2.  If the opponent can win in one move, it plays the third itself to block the opponent to win.
3.  Otherwise, it makes a random move.


### Hard Difficulty
The hard level difficulty will implement a [MinMax](https://en.wikipedia.org/wiki/Minimax) algorithm to create an opponent that's impossible to defeat. 