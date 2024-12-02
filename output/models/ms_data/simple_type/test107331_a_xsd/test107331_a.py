from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from xsdata.models.datatype import (
    XmlDate,
    XmlDateTime,
    XmlDuration,
    XmlPeriod,
    XmlTime,
)


@dataclass
class Anyuri:
    class Meta:
        name = "anyuri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Bool:
    class Meta:
        name = "bool"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Date:
    class Meta:
        name = "date"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Datetime:
    class Meta:
        name = "datetime"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Day:
    class Meta:
        name = "day"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class DecimalType:
    class Meta:
        name = "decimal"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Double:
    class Meta:
        name = "double"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Duration:
    class Meta:
        name = "duration"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Entity:
    class Meta:
        name = "entity"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Float:
    class Meta:
        name = "float"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
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
        },
    )


@dataclass
class Int:
    class Meta:
        name = "int"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Item:
    class Meta:
        name = "item"

    value: Optional[object] = field(default=None)


@dataclass
class Month:
    class Meta:
        name = "month"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Monthday:
    class Meta:
        name = "monthday"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class String:
    class Meta:
        name = "string"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Time:
    class Meta:
        name = "time"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Year:
    class Meta:
        name = "year"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    choice: list[
        Union[
            Entity,
            Anyuri,
            Hexbinary,
            Month,
            Day,
            Monthday,
            Year,
            Date,
            Time,
            Datetime,
            Duration,
            DecimalType,
            Double,
            Float,
            Bool,
            Int,
            String,
            Item,
        ]
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
