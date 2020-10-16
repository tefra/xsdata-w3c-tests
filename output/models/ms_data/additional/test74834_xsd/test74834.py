from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "urn:myxsdschema"


@dataclass
class MyDateTime:
    """
    :ivar date:
    :ivar time:
    :ivar localized_dt:
    """
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
    """
    :ivar date:
    :ivar time:
    :ivar localized_sdt:
    """
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
    """
    :ivar nonstringsection:
    :ivar stringsection:
    """
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
        """
        :ivar bigint:
        :ivar int_value:
        :ivar smallint:
        :ivar tinyint:
        :ivar decimal:
        :ivar numeric:
        :ivar money:
        :ivar smallmoney:
        :ivar float_value:
        :ivar real:
        :ivar datetime:
        :ivar smalldatetime:
        """
        bigint: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        int_value: List[int] = field(
            default_factory=list,
            metadata={
                "name": "int",
                "type": "Element",
                "namespace": "",
            }
        )
        smallint: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        tinyint: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        decimal: List[Decimal] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "total_digits": 38,
                "fraction_digits": 10,
            }
        )
        numeric: List[Decimal] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "total_digits": 38,
                "fraction_digits": 10,
            }
        )
        money: List[Decimal] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_inclusive": -922337203685477.5808,
                "max_inclusive": 922337203685477.5807,
                "total_digits": 19,
                "fraction_digits": 4,
            }
        )
        smallmoney: List[Decimal] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_inclusive": -214748.3648,
                "max_inclusive": 214748.3647,
                "total_digits": 10,
                "fraction_digits": 4,
            }
        )
        float_value: List[Decimal] = field(
            default_factory=list,
            metadata={
                "name": "float",
                "type": "Element",
                "namespace": "",
                "min_inclusive": -1.79E+308,
                "max_inclusive": 1.79E+308,
            }
        )
        real: List[float] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_inclusive": -3.4e+38,
                "max_inclusive": 3.4e+38,
            }
        )
        datetime: List[MyDateTime] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        smalldatetime: List[MySmallDateTime] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )

    @dataclass
    class Stringsection:
        """
        :ivar string:
        """
        string: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "max_length": 4000,
            }
        )
