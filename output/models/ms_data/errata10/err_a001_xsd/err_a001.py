from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class Root:
    """
    :ivar test_byte:
    :ivar test_unsigned_byte:
    :ivar test_integer:
    :ivar test_positive_integer:
    :ivar test_negative_integer:
    :ivar test_non_negative_integer:
    :ivar test_non_positive_integer:
    :ivar test_int:
    :ivar test_unsigned_int:
    :ivar test_long:
    :ivar test_unsigned_long:
    :ivar test_short:
    :ivar test_unsigned_short:
    :ivar test_decimal:
    """
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    test_byte: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testByte",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_unsigned_byte: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testUnsignedByte",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_integer: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testInteger",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_positive_integer: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testPositiveInteger",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_negative_integer: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testNegativeInteger",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_non_negative_integer: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testNonNegativeInteger",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_non_positive_integer: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testNonPositiveInteger",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_int: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testInt",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_unsigned_int: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testUnsignedInt",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_long: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testLong",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_unsigned_long: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testUnsignedLong",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_short: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testShort",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_unsigned_short: List[int] = field(
        default_factory=list,
        metadata={
            "name": "testUnsignedShort",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 0,
        }
    )
    test_decimal: List[Decimal] = field(
        default_factory=list,
        metadata={
            "name": "testDecimal",
            "type": "Element",
            "namespace": "",
            "fraction_digits": 5,
        }
    )
