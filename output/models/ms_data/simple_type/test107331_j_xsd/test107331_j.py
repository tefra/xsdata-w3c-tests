from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import (
    XmlDate,
    XmlDateTime,
    XmlDuration,
    XmlPeriod,
    XmlTime,
)


@dataclass(kw_only=True)
class Anyuri:
    class Meta:
        name = "anyuri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Bool:
    class Meta:
        name = "bool"

    value: bool = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Date:
    class Meta:
        name = "date"

    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Datetime:
    class Meta:
        name = "datetime"

    value: XmlDateTime = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Day:
    class Meta:
        name = "day"

    value: XmlPeriod = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DecimalType:
    class Meta:
        name = "decimal"

    value: Decimal = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Double:
    class Meta:
        name = "double"

    value: float = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Duration:
    class Meta:
        name = "duration"

    value: XmlDuration = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Entity:
    class Meta:
        name = "entity"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Float:
    class Meta:
        name = "float"

    value: float = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Hexbinary:
    class Meta:
        name = "hexbinary"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "format": "base16",
        },
    )


@dataclass(kw_only=True)
class Int:
    class Meta:
        name = "int"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Item:
    class Meta:
        name = "item"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Month:
    class Meta:
        name = "month"

    value: XmlPeriod = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Monthday:
    class Meta:
        name = "monthday"

    value: XmlPeriod = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class String:
    class Meta:
        name = "string"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Time:
    class Meta:
        name = "time"

    value: XmlTime = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Year:
    class Meta:
        name = "year"

    value: XmlPeriod = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    choice: list[
        Entity
        | Anyuri
        | Hexbinary
        | Month
        | Day
        | Monthday
        | Year
        | Date
        | Time
        | Datetime
        | Duration
        | DecimalType
        | Double
        | Float
        | Bool
        | Int
        | String
        | Item
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "entity",
                    "type": Entity,
                },
                {
                    "name": "anyuri",
                    "type": Anyuri,
                },
                {
                    "name": "hexbinary",
                    "type": Hexbinary,
                },
                {
                    "name": "month",
                    "type": Month,
                },
                {
                    "name": "day",
                    "type": Day,
                },
                {
                    "name": "monthday",
                    "type": Monthday,
                },
                {
                    "name": "year",
                    "type": Year,
                },
                {
                    "name": "date",
                    "type": Date,
                },
                {
                    "name": "time",
                    "type": Time,
                },
                {
                    "name": "datetime",
                    "type": Datetime,
                },
                {
                    "name": "duration",
                    "type": Duration,
                },
                {
                    "name": "decimal",
                    "type": DecimalType,
                },
                {
                    "name": "double",
                    "type": Double,
                },
                {
                    "name": "float",
                    "type": Float,
                },
                {
                    "name": "bool",
                    "type": Bool,
                },
                {
                    "name": "int",
                    "type": Int,
                },
                {
                    "name": "string",
                    "type": String,
                },
                {
                    "name": "item",
                    "type": Item,
                },
            ),
        },
    )
