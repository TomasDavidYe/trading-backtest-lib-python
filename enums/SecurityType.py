from enum import Enum


class SecurityType(Enum):
    STOCK = 'STK'
    CASH = 'CASH'
    COMMODITY = 'CMDTY'
    FUTURE = 'FUT'
