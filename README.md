# pybowl

## Requirements:

Create a program in Python that can calculate the score of a full round of bowling, based on user inputs and the following rules:

_Strike_
If you knock down all 10 pins in the first shot of a frame, you get a strike.
How to score: A strike earns 10 points plus the sum of your next two shots.

_Spare_
If you knock down all 10 pins using both shots of a frame, you get a spare.
How to score: A spare earns 10 points plus the sum of your next one shot.

_Open Frame_
If you do not knock down all 10 pins using both shots of your frame (9 or fewer pins knocked down), you have an open frame.
How to score: An open frame only earns the number of pins knocked down.

_The 10th Frame_
If you roll a strike in the first shot of the 10th frame, you get 2 more shots.
If you roll a spare in the first two shots of the 10th frame, you get 1 more shot.
If you leave the 10th frame open after two shots, the game is over and you do not get an additional shot.

How to Score: The score for the 10th frame is the total number of pins knocked down in the 10th frame.

## How to Run

    # To create and start a game
    game = Game()
    game.start_bowling()

## How to test

Just run `pytest` from the root directory
