from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    choice: list[
        Root.TestByte
        | Root.TestUnsignedByte
        | Root.TestInteger
        | Root.TestPositiveInteger
        | Root.TestNegativeInteger
        | Root.TestNonNegativeInteger
        | Root.TestNonPositiveInteger
        | Root.TestInt
        | Root.TestUnsignedInt
        | Root.TestLong
        | Root.TestUnsignedLong
        | Root.TestShort
        | Root.TestUnsignedShort
        | Decimal
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "testByte",
                    "type": ForwardRef("Root.TestByte"),
                    "namespace": "",
                },
                {
                    "name": "testUnsignedByte",
                    "type": ForwardRef("Root.TestUnsignedByte"),
                    "namespace": "",
                },
                {
                    "name": "testInteger",
                    "type": ForwardRef("Root.TestInteger"),
                    "namespace": "",
                },
                {
                    "name": "testPositiveInteger",
                    "type": ForwardRef("Root.TestPositiveInteger"),
                    "namespace": "",
                },
                {
                    "name": "testNegativeInteger",
                    "type": ForwardRef("Root.TestNegativeInteger"),
                    "namespace": "",
                },
                {
                    "name": "testNonNegativeInteger",
                    "type": ForwardRef("Root.TestNonNegativeInteger"),
                    "namespace": "",
                },
                {
                    "name": "testNonPositiveInteger",
                    "type": ForwardRef("Root.TestNonPositiveInteger"),
                    "namespace": "",
                },
                {
                    "name": "testInt",
                    "type": ForwardRef("Root.TestInt"),
                    "namespace": "",
                },
                {
                    "name": "testUnsignedInt",
                    "type": ForwardRef("Root.TestUnsignedInt"),
                    "namespace": "",
                },
                {
                    "name": "testLong",
                    "type": ForwardRef("Root.TestLong"),
                    "namespace": "",
                },
                {
                    "name": "testUnsignedLong",
                    "type": ForwardRef("Root.TestUnsignedLong"),
                    "namespace": "",
                },
                {
                    "name": "testShort",
                    "type": ForwardRef("Root.TestShort"),
                    "namespace": "",
                },
                {
                    "name": "testUnsignedShort",
                    "type": ForwardRef("Root.TestUnsignedShort"),
                    "namespace": "",
                },
                {
                    "name": "testDecimal",
                    "type": Decimal,
                    "namespace": "",
                    "fraction_digits": 5,
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class TestByte:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestUnsignedByte:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestInteger:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestPositiveInteger:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestNegativeInteger:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestNonNegativeInteger:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestNonPositiveInteger:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestInt:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestUnsignedInt:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestLong:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestUnsignedLong:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestShort:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )

    @dataclass(kw_only=True)
    class TestUnsignedShort:
        value: int = field(
            metadata={
                "required": True,
                "fraction_digits": 0,
            }
        )
