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
        self.movement(0, 3)


class JBlock(block_class):
    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            0: [position_class(0, 0), position_class(1, 0), position_class(1, 1), position_class(1, 2)],
            1: [position_class(0, 1), position_class(0, 2), position_class(1, 1), position_class(2, 1)],
            2: [position_class(1, 0), position_class(1, 1), position_class(1, 2), position_class(2, 2)],
            3: [position_class(0, 1), position_class(1, 1), position_class(2, 0), position_class(2, 1)]
        }
        self.movement(0, 3)


class IBlock(block_class):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            0: [position_class(1, 0), position_class(1, 1), position_class(1, 2), position_class(1, 3)],
            1: [position_class(0, 2), position_class(1, 2), position_class(2, 2), position_class(3, 2)],
            2: [position_class(2, 0), position_class(2, 1), position_class(2, 2), position_class(2, 3)],
            3: [position_class(0, 1), position_class(1, 1), position_class(2, 1), position_class(3, 1)]
        }
        self.movement(-1, 3)


class OBlock(block_class):
    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            0: [position_class(0, 0), position_class(0, 1), position_class(1, 0), position_class(1, 1)],
            1: [position_class(0, 0), position_class(0, 2), position_class(1, 0), position_class(1, 1)],
            2: [position_class(0, 0), position_class(0, 1), position_class(1, 0), position_class(1, 1)],
            3: [position_class(0, 0), position_class(0, 1), position_class(1, 0), position_class(1, 1)]
        }
        self.movement(0, 4)


class SBlock(block_class):
    def __init__(self):
        super().__init__(id=5)
        self.cells = {
            0: [position_class(0, 1), position_class(0, 2), position_class(1, 0), position_class(1, 1)],
            1: [position_class(0, 1), position_class(1, 1), position_class(1, 2), position_class(2, 2)],
            2: [position_class(1, 1), position_class(1, 2), position_class(2, 0), position_class(2, 1)],
            3: [position_class(0, 0), position_class(1, 0), position_class(1, 1), position_class(2, 1)]
        }
        self.movement(0, 3)


class TBlock(block_class):
    def __init__(self):
        super().__init__(id=6)
        self.cells = {
            0: [position_class(0, 1), position_class(1, 0), position_class(1, 1), position_class(1, 2)],
            1: [position_class(0, 1), position_class(1, 1), position_class(1, 2), position_class(2, 1)],
            2: [position_class(1, 0), position_class(1, 1), position_class(1, 2), position_class(2, 1)],
            3: [position_class(0, 1), position_class(1, 0), position_class(1, 1), position_class(2, 1)]
        }
        self.movement(0, 3)


class ZBlock(block_class):
    def __init__(self):
        super().__init__(id=7)
        self.cells = {
            0: [position_class(0, 0), position_class(0, 1), position_class(1, 1), position_class(1, 2)],
            1: [position_class(0, 2), position_class(1, 1), position_class(1, 2), position_class(2, 1)],
            2: [position_class(1, 0), position_class(1, 1), position_class(2, 1), position_class(2, 2)],
            3: [position_class(0, 1), position_class(1, 0), position_class(1, 1), position_class(2, 0)]
        }
        self.movement(0, 3)
