from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
import numpy as np

class AIBrain:

    def __init__(self, model_name):
        self.model_name = model_name
        self.model = Sequential()
        layers = [
            Dense(units=200, activation='relu', input_dim=9),
            Dense(units=100, activation='relu'),
            Dense(units=50, activation='relu'),
            Dense(units=25, activation='relu'),
            Dense(units=9, activation='softmax'),
            Dropout(0.05)
        ]

        for layer in layers:
            self.model.add(layer)

        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        try:
            self.model.load_weights(self.filename())
        except IOError:
            pass

    def prompt(self, board, token):
        model_inputs = np.array(board.positions).flatten()
        model_inputs = model_inputs * token
        move_recommendations = self.model.predict(np.array([model_inputs]))[0]
        print move_recommendations
        move_position = np.random.choice(np.arange(9), p=move_recommendations)

        return move_position

    def learn(self, board_positions, valuations):
        print board_positions
        print valuations
        self.model.fit(np.array(board_positions), np.array(valuations), verbose=0)

    def filename(self):
        return "{filename}.hd5".format(filename=self.model_name)

    def save(self):
        self.model.save_weights(self.filename())

