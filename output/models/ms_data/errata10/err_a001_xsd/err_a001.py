from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    choice: list[
        Union[
            "Root.TestByte",
            "Root.TestUnsignedByte",
            "Root.TestInteger",
            "Root.TestPositiveInteger",
            "Root.TestNegativeInteger",
            "Root.TestNonNegativeInteger",
            "Root.TestNonPositiveInteger",
            "Root.TestInt",
            "Root.TestUnsignedInt",
            "Root.TestLong",
            "Root.TestUnsignedLong",
            "Root.TestShort",
            "Root.TestUnsignedShort",
            Decimal,
        ]
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

    @dataclass
    class TestByte:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestUnsignedByte:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestInteger:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestPositiveInteger:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestNegativeInteger:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestNonNegativeInteger:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestNonPositiveInteger:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestInt:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestUnsignedInt:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestLong:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestUnsignedLong:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestShort:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )

    @dataclass
    class TestUnsignedShort:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
                "fraction_digits": 0,
            },
        )
