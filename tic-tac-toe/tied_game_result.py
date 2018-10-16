class TiedGameResult:
    def __init__(self, player1, player2):
        player1.receive_result(0)
        player2.receive_result(0)
