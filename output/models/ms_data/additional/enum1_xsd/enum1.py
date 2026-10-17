from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class EnumType(StrEnum):
    VALUE = "Ѐvalue"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    foo: None | EnumType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    att: None | EnumType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
