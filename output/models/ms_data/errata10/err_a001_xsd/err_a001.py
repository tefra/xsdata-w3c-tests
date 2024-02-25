from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Type, Union

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    choice: List[
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
                    "type": Type["Root.TestByte"],
                    "namespace": "",
                },
                {
                    "name": "testUnsignedByte",
                    "type": Type["Root.TestUnsignedByte"],
                    "namespace": "",
                },
                {
                    "name": "testInteger",
                    "type": Type["Root.TestInteger"],
                    "namespace": "",
                },
                {
                    "name": "testPositiveInteger",
                    "type": Type["Root.TestPositiveInteger"],
                    "namespace": "",
                },
                {
                    "name": "testNegativeInteger",
                    "type": Type["Root.TestNegativeInteger"],
                    "namespace": "",
                },
                {
                    "name": "testNonNegativeInteger",
                    "type": Type["Root.TestNonNegativeInteger"],
                    "namespace": "",
                },
                {
                    "name": "testNonPositiveInteger",
                    "type": Type["Root.TestNonPositiveInteger"],
                    "namespace": "",
                },
                {
                    "name": "testInt",
                    "type": Type["Root.TestInt"],
                    "namespace": "",
                },
                {
                    "name": "testUnsignedInt",
                    "type": Type["Root.TestUnsignedInt"],
                    "namespace": "",
                },
                {
                    "name": "testLong",
                    "type": Type["Root.TestLong"],
                    "namespace": "",
                },
                {
                    "name": "testUnsignedLong",
                    "type": Type["Root.TestUnsignedLong"],
                    "namespace": "",
                },
                {
                    "name": "testShort",
                    "type": Type["Root.TestShort"],
                    "namespace": "",
                },
                {
                    "name": "testUnsignedShort",
                    "type": Type["Root.TestUnsignedShort"],
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
