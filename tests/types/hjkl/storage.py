# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import RootModel


class Key(BaseModel):
    model_config = ConfigDict(extra='forbid')

    string: str
    nat: str


class Value(BaseModel):
    model_config = ConfigDict(extra='forbid')

    sw: str | None
    mr: dict[str, bool] | None


class HjklStorageItem(BaseModel):
    model_config = ConfigDict(extra='forbid')

    key: Key
    value: Value


class HjklStorage(RootModel[Any]):
    root: list[HjklStorageItem]
