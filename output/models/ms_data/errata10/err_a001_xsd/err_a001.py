from decimal import Decimal
from dataclasses import dataclass, field
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
        metadata=dict(
            name="testByte",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_unsigned_byte: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testUnsignedByte",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_integer: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testInteger",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_positive_integer: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testPositiveInteger",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_negative_integer: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testNegativeInteger",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_non_negative_integer: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testNonNegativeInteger",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_non_positive_integer: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testNonPositiveInteger",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_int: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testInt",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_unsigned_int: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testUnsignedInt",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_long: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testLong",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_unsigned_long: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testUnsignedLong",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_short: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testShort",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_unsigned_short: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="testUnsignedShort",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=0
        )
    )
    test_decimal: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            name="testDecimal",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            fraction_digits=5
        )
    )
