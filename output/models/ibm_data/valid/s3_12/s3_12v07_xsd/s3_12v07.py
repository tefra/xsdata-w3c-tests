from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "tns"


@dataclass
class DimType:
    """
    :ivar value:
    :ivar length:
    :ivar width:
    """
    class Meta:
        name = "dimType"

    value: Optional[str] = field(
        default=None,
    )
    length: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class RectType(Enum):
    """
    :cvar LRECTANGLE:
    """
    LRECTANGLE = "lrectangle"


class SquareType(Enum):
    """
    :cvar SQUARE:
    """
    SQUARE = "square"


@dataclass
class Shape:
    """
    :ivar dimension:
    """
    class Meta:
        name = "shape"
        namespace = "tns"

    dimension: List[Union[DimType, RectType, SquareType]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
