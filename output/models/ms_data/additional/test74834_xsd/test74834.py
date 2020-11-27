from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "urn:myxsdschema"


@dataclass
class MyDateTime:
    class Meta:
        name = "myDateTime"

    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2][0-9]:[0-5][0-9]:[0-5][0-9].[0-9][0-9][0-9]",
        }
    )
    localized_dt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class MySmallDateTime:
    class Meta:
        name = "mySmallDateTime"

    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2][0-9]:[0-5][0-9]:[0-5][0-9]",
        }
    )
    localized_sdt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
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
        }
    )
    stringsection: Optional["Datafile.Stringsection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Nonstringsection:
        choice: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "bigint",
                        "type": int,
                        "namespace": "",
                    },
                    {
                        "name": "int",
                        "type": int,
                        "namespace": "",
                    },
                    {
                        "name": "smallint",
                        "type": int,
                        "namespace": "",
                    },
                    {
                        "name": "tinyint",
                        "type": int,
                        "namespace": "",
                    },
                    {
                        "name": "decimal",
                        "type": Decimal,
                        "namespace": "",
                        "total_digits": 38,
                        "fraction_digits": 10,
                    },
                    {
                        "name": "numeric",
                        "type": Decimal,
                        "namespace": "",
                        "total_digits": 38,
                        "fraction_digits": 10,
                    },
                    {
                        "name": "money",
                        "type": Decimal,
                        "namespace": "",
                        "min_inclusive": -922337203685477.5808,
                        "max_inclusive": 922337203685477.5807,
                        "total_digits": 19,
                        "fraction_digits": 4,
                    },
                    {
                        "name": "smallmoney",
                        "type": Decimal,
                        "namespace": "",
                        "min_inclusive": -214748.3648,
                        "max_inclusive": 214748.3647,
                        "total_digits": 10,
                        "fraction_digits": 4,
                    },
                    {
                        "name": "float",
                        "type": Decimal,
                        "namespace": "",
                        "min_inclusive": -1.79E+308,
                        "max_inclusive": 1.79E+308,
                    },
                    {
                        "name": "real",
                        "type": float,
                        "namespace": "",
                        "min_inclusive": -3.4e+38,
                        "max_inclusive": 3.4e+38,
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
            }
        )

    @dataclass
    class Stringsection:
        string: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "max_length": 4000,
            }
        )
