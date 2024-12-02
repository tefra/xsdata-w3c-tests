from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef, Optional, Union

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "urn:myxsdschema"


@dataclass
class MyDateTime:
    class Meta:
        name = "myDateTime"

    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2][0-9]:[0-5][0-9]:[0-5][0-9].[0-9][0-9][0-9]",
        },
    )
    localized_dt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class MySmallDateTime:
    class Meta:
        name = "mySmallDateTime"

    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2][0-9]:[0-5][0-9]:[0-5][0-9]",
        },
    )
    localized_sdt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Datafile:
    class Meta:
        name = "datafile"
        namespace = "urn:myxsdschema"

    nonstringsection: Optional["Datafile.Nonstringsection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    string: list[str] = field(
        default_factory=list,
        metadata={
            "wrapper": "stringsection",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 4000,
        },
    )

    @dataclass
    class Nonstringsection:
        choice: list[
            Union[
                "Datafile.Nonstringsection.Bigint",
                "Datafile.Nonstringsection.Int",
                "Datafile.Nonstringsection.Smallint",
                "Datafile.Nonstringsection.Tinyint",
                "Datafile.Nonstringsection.DecimalType",
                "Datafile.Nonstringsection.Numeric",
                "Datafile.Nonstringsection.Money",
                "Datafile.Nonstringsection.Smallmoney",
                "Datafile.Nonstringsection.Float",
                "Datafile.Nonstringsection.Real",
                MyDateTime,
                MySmallDateTime,
            ]
        ] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "bigint",
                        "type": ForwardRef("Datafile.Nonstringsection.Bigint"),
                        "namespace": "",
                    },
                    {
                        "name": "int",
                        "type": ForwardRef("Datafile.Nonstringsection.Int"),
                        "namespace": "",
                    },
                    {
                        "name": "smallint",
                        "type": ForwardRef(
                            "Datafile.Nonstringsection.Smallint"
                        ),
                        "namespace": "",
                    },
                    {
                        "name": "tinyint",
                        "type": ForwardRef(
                            "Datafile.Nonstringsection.Tinyint"
                        ),
                        "namespace": "",
                    },
                    {
                        "name": "decimal",
                        "type": ForwardRef(
                            "Datafile.Nonstringsection.DecimalType"
                        ),
                        "namespace": "",
                    },
                    {
                        "name": "numeric",
                        "type": ForwardRef(
                            "Datafile.Nonstringsection.Numeric"
                        ),
                        "namespace": "",
                    },
                    {
                        "name": "money",
                        "type": ForwardRef("Datafile.Nonstringsection.Money"),
                        "namespace": "",
                    },
                    {
                        "name": "smallmoney",
                        "type": ForwardRef(
                            "Datafile.Nonstringsection.Smallmoney"
                        ),
                        "namespace": "",
                    },
                    {
                        "name": "float",
                        "type": ForwardRef("Datafile.Nonstringsection.Float"),
                        "namespace": "",
                    },
                    {
                        "name": "real",
                        "type": ForwardRef("Datafile.Nonstringsection.Real"),
                        "namespace": "",
                    },
                    {
                        "name": "datetime",
                        "type": MyDateTime,
                        "namespace": "",
                    },
                    {
                        "name": "smalldatetime",
                        "type": MySmallDateTime,
                        "namespace": "",
                    },
                ),
            },
        )

        @dataclass
        class Bigint:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )

        @dataclass
        class Int:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )

        @dataclass
        class Smallint:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )

        @dataclass
        class Tinyint:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )

        @dataclass
        class DecimalType:
            value: Optional[Decimal] = field(
                default=None,
                metadata={
                    "required": True,
                    "total_digits": 38,
                    "fraction_digits": 10,
                },
            )

        @dataclass
        class Numeric:
            value: Optional[Decimal] = field(
                default=None,
                metadata={
                    "required": True,
                    "total_digits": 38,
                    "fraction_digits": 10,
                },
            )

        @dataclass
        class Money:
            value: Optional[Decimal] = field(
                default=None,
                metadata={
                    "required": True,
                    "min_inclusive": Decimal("-922337203685477.5808"),
                    "max_inclusive": Decimal("922337203685477.5807"),
                    "total_digits": 19,
                    "fraction_digits": 4,
                },
            )

        @dataclass
        class Smallmoney:
            value: Optional[Decimal] = field(
                default=None,
                metadata={
                    "required": True,
                    "min_inclusive": Decimal("-214748.3648"),
                    "max_inclusive": Decimal("214748.3647"),
                    "total_digits": 10,
                    "fraction_digits": 4,
                },
            )

        @dataclass
        class Float:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "required": True,
                    "min_inclusive": -1.79e308,
                    "max_inclusive": 1.79e308,
                },
            )

        @dataclass
        class Real:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "required": True,
                    "min_inclusive": -3.4e38,
                    "max_inclusive": 3.4e38,
                },
            )
