import random
import csv

class TicTacToe:
    def __init__(self, playerX, playerO):
        self.board = [' ']*9
        self.playerX, self.playerO = playerX, playerO
        self.playerX_turn = True
        self.invalid_moves = 0

    def play_game(self):
        self.playerX.start_game('X')
        self.playerO.start_game('O')
        while True: #yolo
            if self.playerX_turn:
                player, char, other_player = self.playerX, 'X', self.playerO
            else:
                player, char, other_player = self.playerO, 'O', self.playerX

            self.display_board()

            space = player.move(self.board)
            # print "Player {char} picks {space}!".format(char=char, space=space)

            if self.board[space-1] != ' ': # illegal move
                # print "Invalid move! Try again!"
                self.invalid_moves += 1
                player.reward(-99, self.board) # score of shame
                break
            self.board[space-1] = char
            if self.player_wins(char):
                self.display_board()
                player.reward(1, self.board)
                other_player.reward(-1, self.board)
                self.winner = char
                # print "Player {char} wins!".format(char=char)
                break
            if self.board_full(): # tie game
                self.display_board()
                player.reward(0.5, self.board)
                other_player.reward(0.5, self.board)
                self.winner = None
                # print "Tie!"
                break
            other_player.reward(0, self.board)
            self.playerX_turn = not self.playerX_turn

        # print "\n\n\n"

    def player_wins(self, char):
        for a,b,c in [(0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8),
                      (0,4,8), (2,4,6)]:
            if char == self.board[a] == self.board[b] == self.board[c]:
                return True
        return False

    def board_full(self):
        return not any([space == ' ' for space in self.board])

    def display_board(self):
        row = " {} | {} | {}"
        hr = "\n-----------\n"
        # print (row + hr + row + hr + row).format(*self.board)
        # print "=============="


class Player(object):
    def __init__(self):
        self.breed = "human"

    def start_game(self, char):
        # print "\nNew game!"
        pass

    def move(self, board):
        return int(raw_input("Your move? "))

    def reward(self, value, board):
        # print "{} rewarded: {}".format(self.breed, value)
        pass

    def available_moves(self, board):
        return [i+1 for i in range(0,9) if board[i] == ' ']

class QLearningPlayer(Player):
    def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9):
        self.breed = "Qlearner"

        self.epsilon = epsilon # e-greedy chance of random exploration
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor for future rewards
        self.load()

    def load(self):
        self.q = {}
        try:
            with open('q-data.csv', mode='r') as infile:
                reader = csv.reader(infile)
                self.q = {((rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rows[8]), rows[9]): rows[10] for rows in reader}
        except IOError:
            pass

    def save(self):
        with open('q-data.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            for key in self.q:
                ((slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9), action) = key
                writer.writerow([slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, action, self.q[key]])

    def start_game(self, char):
        self.last_board = (' ',)*9
        self.last_move = None

    def getQ(self, state, action):
        # encourage exploration; "optimistic" 1.0 initial values
        if self.q.get((state, action)) is None:
            self.q[(state, action)] = 1.0
        return self.q.get((state, action))

    def move(self, board):
        self.last_board = tuple(board)
        actions = self.available_moves(board)

        if random.random() < self.epsilon: # explore!
            # print "random choice!"
            self.last_move = random.choice(actions)
            return self.last_move

        qs = [self.getQ(self.last_board, a) for a in actions]
        # print zip(actions, qs)
        maxQ = max(qs)

        if qs.count(maxQ) > 1:
            # more than 1 best option; choose among them randomly
            best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
            i = random.choice(best_options)
        else:
            i = qs.index(maxQ)

        self.last_move = actions[i]
        return actions[i]

    def reward(self, value, board):
        if self.last_move:
            self.learn(self.last_board, self.last_move, value, tuple(board))

    def learn(self, state, action, reward, result_state):
        prev = self.getQ(state, action)
        maxqnew = max([self.getQ(result_state, a) for a in self.available_moves(state)])
        self.q[(state, action)] = prev + self.alpha * ((reward + self.gamma*maxqnew) - prev)

class StaticPlayer(QLearningPlayer):
    def learn(self, state, action, reward, result_state):
        pass

p1 = QLearningPlayer()
p2 = StaticPlayer()

N_EPOCHS = 2
N_ROUNDS = 10

with open("q-outcomes.csv", 'ab') as csvfile:
    csv_writer = csv.writer(csvfile)
    for j in xrange(N_EPOCHS):

        print "BEFORE LOAD"
        print p1.q
        print "\n" * 20
        print p2.q
        print p1.q == p2.q
        p1.save()
        p2.load()
        print "AFTER LOAD"
        print p1.q
        print "\n" * 20
        print p2.q
        print p1.q == p2.q

        for i in xrange(N_ROUNDS):
            print "Epoch {j}, Game {i}".format(j=j, i=i)
            if i % 2 == 0:
                t = TicTacToe(p1, p2)
            else:
                t = TicTacToe(p2, p1)
            t.play_game()
            if t.winner:
                if i % 2 == 0:
                    csv_writer.writerow([int(t.winner == 'X'), t.invalid_moves])
                else:
                    csv_writer.writerow([int(t.winner == 'O'), t.invalid_moves])
            else:
                csv_writer.writerow([0.5, t.invalid_moves])

