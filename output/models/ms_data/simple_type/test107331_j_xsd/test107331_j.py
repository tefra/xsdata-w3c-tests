from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod, XmlTime


@dataclass
class Anyuri:
    class Meta:
        name = "anyuri"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Bool:
    class Meta:
        name = "bool"

    value: Optional[bool] = field(
        default=None
    )


@dataclass
class Date:
    class Meta:
        name = "date"

    value: Optional[XmlDate] = field(
        default=None
    )


@dataclass
class Datetime:
    class Meta:
        name = "datetime"

    value: Optional[XmlDateTime] = field(
        default=None
    )


@dataclass
class Day:
    class Meta:
        name = "day"

    value: Optional[XmlPeriod] = field(
        default=None
    )


@dataclass
class DecimalType:
    class Meta:
        name = "decimal"

    value: Optional[Decimal] = field(
        default=None
    )


@dataclass
class Double:
    class Meta:
        name = "double"

    value: Optional[float] = field(
        default=None
    )


@dataclass
class Duration:
    class Meta:
        name = "duration"

    value: Optional[XmlDuration] = field(
        default=None
    )


@dataclass
class Entity:
    class Meta:
        name = "entity"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Float:
    class Meta:
        name = "float"

    value: Optional[float] = field(
        default=None
    )


@dataclass
class Hexbinary:
    class Meta:
        name = "hexbinary"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "format": "base16",
        }
    )


@dataclass
class Int:
    class Meta:
        name = "int"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class Item:
    class Meta:
        name = "item"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Month:
    class Meta:
        name = "month"

    value: Optional[XmlPeriod] = field(
        default=None
    )


@dataclass
class Monthday:
    class Meta:
        name = "monthday"

    value: Optional[XmlPeriod] = field(
        default=None
    )


@dataclass
class String:
    class Meta:
        name = "string"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Time:
    class Meta:
        name = "time"

    value: Optional[XmlTime] = field(
        default=None
    )


@dataclass
class Year:
    class Meta:
        name = "year"

    value: Optional[XmlPeriod] = field(
        default=None
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    entity: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    anyuri: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    hexbinary: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "format": "base16",
        }
    )
    month: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    day: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    monthday: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    year: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    date: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    time: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    datetime: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    duration: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    decimal: List[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    double: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    float_value: List[float] = field(
        default_factory=list,
        metadata={
            "name": "float",
            "type": "Element",
        }
    )
    bool_value: List[bool] = field(
        default_factory=list,
        metadata={
            "name": "bool",
            "type": "Element",
        }
    )
    int_value: List[int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
        }
    )
    string: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    item: List[Item] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
