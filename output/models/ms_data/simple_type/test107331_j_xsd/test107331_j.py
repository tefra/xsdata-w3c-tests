from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod, XmlTime


@dataclass
class Anyuri:
    class Meta:
        name = "anyuri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Bool:
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

    value: Optional[float] = field(
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

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Float:
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
class Int:
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
class String:
    class Meta:
        name = "string"

    value: str = field(
        default="",
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


@dataclass
class Root:
    class Meta:
        name = "root"

    choice: List[Union[str, XmlDateTime, Decimal, int, float, bytes, bool, XmlPeriod, XmlDate, Item, XmlTime, XmlDuration]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "entity",
                    "type": str,
                },
                {
                    "name": "anyuri",
                    "type": str,
                },
                {
                    "name": "hexbinary",
                    "type": bytes,
                    "format": "base16",
                },
                {
                    "name": "month",
                    "type": XmlPeriod,
                },
                {
                    "name": "day",
                    "type": XmlPeriod,
                },
                {
                    "name": "monthday",
                    "type": XmlPeriod,
                },
                {
                    "name": "year",
                    "type": XmlPeriod,
                },
                {
                    "name": "date",
                    "type": XmlDate,
                },
                {
                    "name": "time",
                    "type": XmlTime,
                },
                {
                    "name": "datetime",
                    "type": XmlDateTime,
                },
                {
                    "name": "duration",
                    "type": XmlDuration,
                },
                {
                    "name": "decimal",
                    "type": Decimal,
                },
                {
                    "name": "double",
                    "type": float,
                },
                {
                    "name": "float",
                    "type": float,
                },
                {
                    "name": "bool",
                    "type": bool,
                },
                {
                    "name": "int",
                    "type": int,
                },
                {
                    "name": "string",
                    "type": str,
                },
                {
                    "name": "item",
                    "type": Item,
                },
            ),
        }
    )
