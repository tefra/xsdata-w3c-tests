from enum import Enum
from dataclasses import dataclass, field
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
    length: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    width: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
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
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
