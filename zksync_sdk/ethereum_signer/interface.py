from abc import ABC, abstractmethod

from zksync_sdk.types import EncodedTx, TxEthSignature

__all__ = ['EthereumSignerInterface']


class EthereumSignerInterface(ABC):

    @abstractmethod
    async def sign_tx(self, tx: EncodedTx) -> TxEthSignature:
        raise NotImplementedError

    @abstractmethod
    async def sign(self, message: bytes) -> TxEthSignature:
        raise NotImplementedError

    @abstractmethod
    def address(self) -> str:
        raise NotImplementedError
