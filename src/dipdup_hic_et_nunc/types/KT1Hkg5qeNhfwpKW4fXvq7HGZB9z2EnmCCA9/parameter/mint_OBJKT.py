# generated by datamodel-codegen:
#   filename:  mint_OBJKT.json

from __future__ import annotations

from pydantic import BaseModel


class MintObjkt(BaseModel):
    address: str
    amount: str
    metadata: str
    royalties: str