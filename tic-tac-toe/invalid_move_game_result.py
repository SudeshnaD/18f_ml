class InvalidMoveGameResult:
    def __init__(self, invalid_mover):
        invalid_mover.receive_result(-1)

