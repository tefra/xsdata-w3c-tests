from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class MyEnum(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


@dataclass(kw_only=True)
class Regex:
    att: None | MyEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[13]",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: list[Regex] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
