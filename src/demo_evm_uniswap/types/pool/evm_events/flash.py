# generated by DipDup 8.0.0b2

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class FlashPayload(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    sender: str
    recipient: str
    amount0: int
    amount1: int
    paid0: int
    paid1: int