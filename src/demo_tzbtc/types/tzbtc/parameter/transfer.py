# generated by datamodel-codegen:
#   filename:  transfer.json

from __future__ import annotations

from pydantic import BaseModel, Field


class TransferParameter(BaseModel):
    from_: str = Field(..., alias='from')
    to: str
    value: str