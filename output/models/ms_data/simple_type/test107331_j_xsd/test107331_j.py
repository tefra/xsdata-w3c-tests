from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class Anyuri:
    """
    :ivar value:
    """
    class Meta:
        name = "anyuri"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class BoolType:
    """
    :ivar value:
    """
    class Meta:
        name = "bool"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Date:
    """
    :ivar value:
    """
    class Meta:
        name = "date"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Datetime:
    """
    :ivar value:
    """
    class Meta:
        name = "datetime"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Day:
    """
    :ivar value:
    """
    class Meta:
        name = "day"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Decimal:
    """
    :ivar value:
    """
    class Meta:
        name = "decimal"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Double:
    """
    :ivar value:
    """
    class Meta:
        name = "double"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Duration:
    """
    :ivar value:
    """
    class Meta:
        name = "duration"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Entity:
    """
    :ivar value:
    """
    class Meta:
        name = "entity"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class FloatType:
    """
    :ivar value:
    """
    class Meta:
        name = "float"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Hexbinary:
    """
    :ivar value:
    """
    class Meta:
        name = "hexbinary"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class IntType:
    """
    :ivar value:
    """
    class Meta:
        name = "int"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Item:
    """
    :ivar any_element:
    """
    class Meta:
        name = "item"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Month:
    """
    :ivar value:
    """
    class Meta:
        name = "month"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Monthday:
    """
    :ivar value:
    """
    class Meta:
        name = "monthday"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class String:
    """
    :ivar value:
    """
    class Meta:
        name = "string"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Time:
    """
    :ivar value:
    """
    class Meta:
        name = "time"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Year:
    """
    :ivar value:
    """
    class Meta:
        name = "year"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar entity:
    :ivar anyuri:
    :ivar hexbinary:
    :ivar month:
    :ivar day:
    :ivar monthday:
    :ivar year:
    :ivar date:
    :ivar time:
    :ivar datetime:
    :ivar duration:
    :ivar decimal:
    :ivar double:
    :ivar float_value:
    :ivar bool_value:
    :ivar int_value:
    :ivar string:
    :ivar item:
    """
    class Meta:
        name = "root"

    entity: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    anyuri: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    hexbinary: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    month: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    day: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    monthday: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    year: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    date: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    time: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    datetime: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    duration: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    decimal: List[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    double: List[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    float_value: List[float] = field(
        default_factory=list,
        metadata={
            "name": "float",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    bool_value: List[bool] = field(
        default_factory=list,
        metadata={
            "name": "bool",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    int_value: List[int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    string: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    item: List[Item] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
