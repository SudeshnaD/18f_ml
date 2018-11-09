from keras.models import Sequential
from keras.layers import Dense
import numpy as np

class AIBrain:

    def __init__(self, model_name):
        self.model_name = model_name
        self.model = Sequential()
        layers = [
            Dense(units=200, activation='relu', input_dim=9),
            Dense(units=300, activation='relu'),
            Dense(units=500, activation='relu'),
            Dense(units=300, activation='relu'),
            Dense(units=200, activation='relu'),
            Dense(units=100, activation='relu'),
            Dense(units=50, activation='relu'),
        ]

        for layer in layers:
            self.model.add(layer)

        OutputLayer = Dense(units=9, activation='softmax')
        self.model.add(OutputLayer)
        self.model.load_weights(self.filename())
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    def prompt(self, board):
        model_inputs = np.array(board.positions).flatten()
        move_recommendations = self.model.predict(np.array([model_inputs]))[0]
        move_position = np.random.choice(np.arange(9), p=move_recommendations)

        return move_position

    def learn(self, board, move, result):
        pass

    def filename(self):
        return "{filename}.hd5".format(filename=self.model_name)

    def save(self):
        self.model.save_weights(self.filename())

