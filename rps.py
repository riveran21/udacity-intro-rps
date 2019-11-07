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
    announce = ["Rock", "Paper!", "Scissors!!", "SHOOT!!!"]

    def move(self):
        print("""
        Time to shoot your move! Will it be...

        Rock... Paper... or Scissors...

        You may also enter "Q" or "Quit" to exit the game.
        """)

        shoot = input("""
        Rock, Paper or Scissors:  """).lower()

        while shoot not in moves:
            if shoot in ["quit", "q"]:
                quitGame()
                # print("""
                # Thank you for playing my game! Bye now!!
                # """)
                # exit(0)
            else:
                print("""
                Well that's not gonna work. Give it another go!

                Enter Rock, Paper or Scissors or Q or Quit to Exit.

                SHOOT!!
                """)
                shoot = input("""
                Rock, Paper or Scissors:  """).lower()

        for mv in self.announce:
            # print(n, end=' ')
            print(mv)
            time.sleep(1)

        return shoot


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

        Player 1: {move1}
        Player 2: {move2}

        """)
        if move1 == move2:
            self.score1 += 1
            self.score2 += 1
            print(f"""
            A tie. How boring... 1-Point each.

            The score is now...
            Player 1:\t{self.score1}
            Player 2:\t{self.score2}
            """)
        elif beats(move1, move2):
            self.score1 += 2
            print(f"""
            Player 1 Wins!
            2-Points to Player 1!!

            The score is now...
            Player 1:\t{self.score1}
            Player 2:\t{self.score2}
            """)
        else:
            self.score2 += 2
            print(f"""
            Player 2 Wins!
            2-Points to Player 2!!

            The score is now...
            Player 1:\t{self.score1}
            Player 2:\t{self.score2}
            """)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("""
        Please enter the number of rounds you would
        to play this match.

        You may also choose to quit the game by entering
        'Q' or 'Quit'.
        """)

        lastRound = input("Rounds:  ").lower()

        while lastRound.isdigit() is False:
            if lastRound in ["quit", "q"]:
                quitGame()
            else:
                print("""
                Please enter a number or 'q' or 'quit'
                to exit the game.
                """)

                lastRound = input("Rounds:  ").lower()

        print("""
        We have a game!!

        Get Ready to Shoot!!
        """)
        for round in range(1, int(lastRound) + 1):
            print(f"Round {round}:")
            self.play_round()
        if self.score1 == self.score2:
            print(f"""
            That's the game and our final score is...

            Player 1:  {self.score1}
            Player 2:  {self.score2}

            A Tie! Congratulations to both our winners.
            We only have one prize, so you'll have to
            arm wrestle for it.

            Thanks! for playing!!
            """)

            whichGame()

        elif self.score1 > self.score2:
            print(f"""
            That's the game and our final score is...

            Player 1:  {self.score1}
            Player 2:  {self.score2}

            And the big winner is... Player 1!

            Congratulations to Player 1!
            For Player 2 we have some nice parting gifts...
                ...where did I put them...
                ...we'll have to mail them to you.

            Thank you for playing our game!

            Until next time keep those fingers nimble!
            """)

            whichGame()
        else:
            print(f"""
            That's the game and our final score is...

            Player 1:  {self.score1}
            Player 2:  {self.score2}

            And the big winner is... Player 2!

            Congratulations to Player 2!
            For Player 1 we have some nice parting gifts...
                ...where did I put them...
                ...we'll have to mail them to you.

            Thank you for playing our game!

            Until next time keep those fingers nimble!
            """)

            whichGame()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def quitGame():
    print(f"""
    I LOOK FORWARD TO OUR NEXT ADVENTURE.

    UNTIL NEXT TIME PROFESSOR {playerName}.

    GOODBYE.""")

    exit(0)


def shallWe():
    shallWePlay = input(f"""
    GREETINGS PROFESSOR {playerName}.

    SHALL WE PLAY A GAME (YES OR NO)?  """).lower()

    while shallWePlay not in ["yes", "no"]:
        shallWePlay = input("""
        PLEASE ENTER "YES" OR "NO"

        SHALL WE PLAY A GAME?  """).lower()

    if shallWePlay == "no":
        quitGame()
    else:
        print("""
        EXCELLENT. IT'S BEEN A WHILE SINCE I'VE
        PLAYED A GOOD GAME OF CHESS.
        """)

        whichGame()


def whichGame():
    whichGameOptions = ["1", "2", "3", "4"]

    print("""
    WHICH GAME WOULD YOU LIKE TO PLAY?

        1. Rock, Paper, Scissors
        2. Tic Tac Toe
        3. Global Thermonuclear War
        4. Quit Game
        """)

    whichGameNumber = input("ENTER MENU NUMBER:  ")

    while whichGameNumber not in whichGameOptions:
        print("""
        PLEASE CHOOSE OPTION BETWEEN 1-3
        OR CHOOSE 4 TO QUIT GAME.

        WHICH GAME WOULD YOU LIKE TO PLAY?

            1. Rock, Paper, Scissors
            2. Tic Tac Toe
            3. Global Thermonuclear War
            4. Quit Game
        """)

        whichGameNumber = input("ENTER MENU NUMBER:  ")

    if whichGameNumber in ["2", "3"]:
        funnyGuy(whichGameNumber)
    elif whichGameNumber == "4":
        quitGame()
    else:
        selectPlayers()


def funnyGuy(whichGameNumber):
    if whichGameNumber == "2":
        print("""
        NO ONE EVER WINS AT TIC TAC TOE.

        LET US CHOOSE A DIFFERENT GAME.

        A GAME OF WITS PERHAPS.

        BUT SINCE WE DO NOT HAVE CHESS,
        MAY I SUGGEST "ROCK, PAPER, SCISSORS"
        """)

        whichGame()

    elif whichGameNumber == "3":
        n = 10
        while n > 0:
            print(n)
            n -= 1
            time.sleep(1)
        print(f"""
        K A B L O O M!!!

        WELL THAT WAS FUN.

        I WOULD SAY THIS GAME IS A LITTLE LIKE
        OUR CURRENT PRESIDENT...

        WHILE THE NAME MAY SOUND COOL... IT'S REALLY A
        DISASTER WAITING TO HAPPEN.

        POLITICS ASIDE... THAT WAS A FUNNY JOKE.

        HA HA HA HA!!

        LET'S CHOOSE ANOTHER GAME, SHALL WE.
        """)

        whichGame()


def selectPlayers():
    selectPlayerOptions = ["1", "2", "3", "4", "5"]

    print(f"""
    EXCELLENT CHOICE PROFESSOR {playerName}!!

    THERE ARE FIVE PLAYER TYPES, (1) HUMAN TYPE
    AND (4) COMPUTER PLAYER TYPES.

    PLEASE CHOOSE THE FIRST PLAYER TYPE FROM MENU BELOW:

        1. PROFESSOR {playerName}
        2. The Rock (CPU)
        3. The Enigma (CPU)
        4. The Mirror (CPU)
        5. The Cycle (CPU)
    """)

    readyPlayer1 = input("""SELECT PLAYER 1:  """)

    while readyPlayer1 not in selectPlayerOptions:
        readyPlayer1 = input("""
        PLEASE CHOOSE AN OPTION BETWEEN 1-5

        SELECT PLAYER 1:  """)

    if readyPlayer1 == "1":
        readyPlayer1 = HumanPlayer()
    elif readyPlayer1 == "2":
        readyPlayer1 = Player()
    elif readyPlayer1 == "3":
        readyPlayer1 = RandomPlayer()
    elif readyPlayer1 == "4":
        readyPlayer1 = ReflectPlayer()
    else:
        readyPlayer1 = CyclePlayer()

    print(f"""
    EXCELLENT CHOICE {playerName}. LET'S CHOOSE A SECOND
    PLAYER TYPE FROM THE SAME LIST...

        1. PROFESSOR {playerName}
        2. The Rock (CPU)
        3. The Enigma (CPU)
        4. The Mirror (CPU)
        5. The Cycle (CPU)
    """)

    readyPlayer2 = input("""SELECT PLAYER 2:  """)

    while readyPlayer2 not in selectPlayerOptions:
        readyPlayer2 = input("""
        PLEASE CHOOSE AN OPTION BETWEEN 1-5

        SELECT PLAYER 2:  """)

    if readyPlayer2 == "1":
        readyPlayer2 = HumanPlayer()
    elif readyPlayer2 == "2":
        readyPlayer2 = Player()
    elif readyPlayer2 == "3":
        readyPlayer2 = RandomPlayer()
    elif readyPlayer2 == "4":
        readyPlayer2 = ReflectPlayer()
    else:
        readyPlayer2 = CyclePlayer()

    game = Game(readyPlayer1, readyPlayer2)
    game.play_game()


if __name__ == '__main__':
    playerName = input("""
    What is your name?  """).upper()

    shallWe()

    # game = Game(HumanPlayer(), Player())
    # game.play_game()
