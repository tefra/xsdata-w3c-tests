from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ArrayType:
    class Meta:
        name = "arrayType"

    ele: list[str] = field(
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
class Root(ArrayType):
    class Meta:
        name = "root"
