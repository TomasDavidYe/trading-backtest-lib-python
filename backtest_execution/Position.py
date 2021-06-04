from enums.PositionType import PositionType


class Position:
    def __init__(self, symbol: str, position_type: PositionType, open_price: float, quantity: float = None):
        self.open_price = open_price
        self.quantity = quantity
        self.position_type = position_type
        self.symbol = symbol
