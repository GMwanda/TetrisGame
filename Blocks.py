from BlockClass import block_class
from PositionClass import position_class


class LBlock(block_class):
    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            0: [position_class(0, 2), position_class(1, 0), position_class(1, 1), position_class(1, 2)],
            1: [position_class(0, 1), position_class(1, 1), position_class(3, 1), position_class(3, 2)],
            2: [position_class(1, 0), position_class(1, 1), position_class(1, 2), position_class(3, 0)],
            3: [position_class(0, 0), position_class(0, 1), position_class(1, 1), position_class(3, 1)]
        }


class JBlock(block_class):
    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            0: [position_class(0, 0), position_class(1, 0), position_class(1, 1), position_class(1, 2)],
            1: [position_class(0, 1), position_class(0, 2), position_class(1, 1), position_class(2, 1)],
            2: [position_class(1, 0), position_class(1, 1), position_class(1, 2), position_class(2, 2)],
            3: [position_class(0, 1), position_class(1, 1), position_class(2, 0), position_class(2, 1)]
        }


class IBlock(block_class):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            0: [position_class(0, 0), position_class(1, 0), position_class(1, 1), position_class(1, 2)],
            1: [position_class(0, 1), position_class(0, 2), position_class(1, 1), position_class(2, 1)],
            2: [position_class(1, 0), position_class(1, 1), position_class(1, 2), position_class(2, 2)],
            3: [position_class(0, 1), position_class(1, 1), position_class(2, 0), position_class(2, 1)]
        }
