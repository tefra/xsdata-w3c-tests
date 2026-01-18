from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ArrayType:
    entry: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    length: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Xlist(ArrayType):
    class Meta:
        name = "XList"
