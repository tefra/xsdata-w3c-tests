from dataclasses import dataclass, field
from typing import Optional, Union

__NAMESPACE__ = "tns"


@dataclass
class DimType:
    class Meta:
        name = "dimType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    length: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
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


@dataclass
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


@dataclass
class Shape:
    class Meta:
        name = "shape"
        namespace = "tns"

    dimension: list[Union[DimType, RectType, SquareType]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
