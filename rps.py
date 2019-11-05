#!/usr/bin/env python3
import random
import time


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    pause = time.sleep(.5)

    def move(self):
        shoot = input("""
        Enter 'Rock, Paper or Scissors'\
('q' or 'quit' to End Game)>  """).lower()
        if shoot in ["quit", "q"]:
            print("""
            Thank you for playing today. Bye now!!
            """)
            exit(0)
        elif shoot in moves:
            print(f"""
    Rock {self.pause} Paper! {self.pause} Scissors!! {self.pause}
    S H O O T!!!
    {self.pause}
    """)
            return shoot
        else:
            self.move()


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move is "rock":
            return "paper"
        elif self.my_move is "paper":
            return "scissors"
        elif self.my_move is "scissors":
            return "rock"
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    score1 = 0
    score2 = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"""

    Player 1: {move1} Player 2: {move2}

    """)
        if move1 == move2:
            self.score1 += 1
            self.score2 += 1
            print(f"""
    Tie. How boring... 1-Point each.

    Score is now {self.score1} to {self.score2}...

    Moving on...
    """)
        elif beats(move1, move2):
            self.score1 += 2
            print(f"""
    Player 1 Wins! That's 2-Points to the Winner!!

    The score is now {self.score1} to {self.score2}.
    """)
        else:
            self.score2 += 2
            print(f"""
    Player 2 Wins! That's 2 more points for you!

    Score is {self.score1} to {self.score2}.
    """)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        LastRound = int(input("""
How many rounds this game?  """))
        print("""
Get Ready to Shoot!!
""")
        for round in range(1, LastRound+1):
            print(f"Round {round}:")
            self.play_round()
        if self.score1 == self.score2:
            print(f"""
    That's the game and we have a tie! The final score is...

    Player 1: {self.score1} pts. to Player 2: {self.score2} pts.

    Thanks! for playing!!
            """)
        elif self.score1 > self.score2:
            print(f"""
    That's all she wrote and today's winner is Player1

    With a score of {self.score1} pts. to {self.score2} pts.!

    Until next time keep those fingers nimble!
            """)
        else:
            print(f"""
    By a margin of {self.score2 - self.score1} points,
    today's winner is Player 2!! The final score was...

    Player 2: {self.score2} to Player 1: {self.score1}!

    Come back and play again soon!!
            """)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    game1 = Game(Player(), Player())
    game1.play_game()

    game2 = Game(RandomPlayer(), RandomPlayer())
    game2.play_game()

    game3 = Game(RandomPlayer(), ReflectPlayer())
    game3.play_game()

    game4 = Game(RandomPlayer(), CyclePlayer())
    game4.play_game()

    game5 = Game(HumanPlayer(), RandomPlayer())
    game5.play_game()

    game6 = Game(HumanPlayer(), ReflectPlayer())
    game6.play_game()

    game7 = Game(HumanPlayer(), CyclePlayer())
    game7.play_game()
