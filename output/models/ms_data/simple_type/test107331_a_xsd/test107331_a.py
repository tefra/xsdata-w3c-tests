from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod, XmlTime


@dataclass
class Anyuri:
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
    class Meta:
        name = "date"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Datetime:
    class Meta:
        name = "datetime"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Day:
    class Meta:
        name = "day"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class DecimalType:
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
    class Meta:
        name = "duration"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Entity:
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
    class Meta:
        name = "hexbinary"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base16",
        }
    )


@dataclass
class IntType:
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
    class Meta:
        name = "item"

    value: Optional[object] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Month:
    class Meta:
        name = "month"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Monthday:
    class Meta:
        name = "monthday"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
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
    hexbinary: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "format": "base16",
        }
    )
    month: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    day: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    monthday: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    year: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    date: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    time: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    datetime: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    duration: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    decimal_value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "name": "decimal",
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
    item: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class String:
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
    class Meta:
        name = "time"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Year:
    class Meta:
        name = "year"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
