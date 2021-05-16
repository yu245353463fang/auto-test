from enum import IntEnum

from .responses import *
from .signatures import *
from .transactions import *


class ChainId(IntEnum):
    MAINNET = 1
    RINKEBY = 4
    ROPSTEN = 3
    LOCALHOST = 9
