from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "tns"


@dataclass(kw_only=True)
class DimType:
    class Meta:
        name = "dimType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    length: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class RectType(DimType):
    class Meta:
        name = "rectType"

    value: str = field(
        init=False,
        default="lrectangle",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SquareType(DimType):
    class Meta:
        name = "squareType"

    value: str = field(
        init=False,
        default="square",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Shape:
    class Meta:
        name = "shape"
        namespace = "tns"

    dimension: list[DimType | RectType | SquareType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
