from enum import Enum


class OrderType(Enum):
    LIMIT = 'LMT'
    MARKET = 'MKT'
    MTL = 'MTL'
    MIT = 'MIT'
    LIT = 'LIT'
    LOC = 'LOC'
    MOC = 'MOC'
    PEG_MKT = 'PEG MKT'
    PEG_STK = 'PEG STK'
    REL = 'REL'
    BOX_TOP = 'BOX TOP'



