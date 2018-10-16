class WinningGameResult:
    def __init__(self, winner, loser):
        winner.receive_result(1)
        loser.receive_result(-1)
