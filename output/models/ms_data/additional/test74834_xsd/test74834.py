from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "urn:myxsdschema"


@dataclass(kw_only=True)
class MyDateTime:
    class Meta:
        name = "myDateTime"

    date: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    time: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2][0-9]:[0-5][0-9]:[0-5][0-9].[0-9][0-9][0-9]",
        }
    )
    localized_dt: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class MySmallDateTime:
    class Meta:
        name = "mySmallDateTime"

    date: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    time: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2][0-9]:[0-5][0-9]:[0-5][0-9]",
        }
    )
    localized_sdt: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Datafile:
    class Meta:
        name = "datafile"
        namespace = "urn:myxsdschema"

    nonstringsection: Datafile.Nonstringsection = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    stringsection: Datafile.Stringsection = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass(kw_only=True)
    class Nonstringsection:
        choice: list[
            Datafile.Nonstringsection.Bigint
            | Datafile.Nonstringsection.Int
            | Datafile.Nonstringsection.Smallint
            | Datafile.Nonstringsection.Tinyint
            | Datafile.Nonstringsection.DecimalType
            | Datafile.Nonstringsection.Numeric
            | Datafile.Nonstringsection.Money
            | Datafile.Nonstringsection.Smallmoney
            | Datafile.Nonstringsection.Float
            | Datafile.Nonstringsection.Real
            | MyDateTime
            | MySmallDateTime
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

        @dataclass(kw_only=True)
        class Bigint:
            value: int = field()

        @dataclass(kw_only=True)
        class Int:
            value: int = field()

        @dataclass(kw_only=True)
        class Smallint:
            value: int = field()

        @dataclass(kw_only=True)
        class Tinyint:
            value: int = field()

        @dataclass(kw_only=True)
        class DecimalType:
            value: Decimal = field(
                metadata={
                    "total_digits": 38,
                    "fraction_digits": 10,
                }
            )

        @dataclass(kw_only=True)
        class Numeric:
            value: Decimal = field(
                metadata={
                    "total_digits": 38,
                    "fraction_digits": 10,
                }
            )

        @dataclass(kw_only=True)
        class Money:
            value: Decimal = field(
                metadata={
                    "min_inclusive": Decimal("-922337203685477.5808"),
                    "max_inclusive": Decimal("922337203685477.5807"),
                    "total_digits": 19,
                    "fraction_digits": 4,
                }
            )

        @dataclass(kw_only=True)
        class Smallmoney:
            value: Decimal = field(
                metadata={
                    "min_inclusive": Decimal("-214748.3648"),
                    "max_inclusive": Decimal("214748.3647"),
                    "total_digits": 10,
                    "fraction_digits": 4,
                }
            )

        @dataclass(kw_only=True)
        class Float:
            value: float = field(
                metadata={
                    "min_inclusive": -1.79e308,
                    "max_inclusive": 1.79e308,
                }
            )

        @dataclass(kw_only=True)
        class Real:
            value: float = field(
                metadata={
                    "min_inclusive": -3.4e38,
                    "max_inclusive": 3.4e38,
                }
            )

    @dataclass(kw_only=True)
    class Stringsection:
        string: list[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "max_length": 4000,
            },
        )
