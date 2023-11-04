from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Union

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    choice: List[Union[int, Decimal]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "testByte",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testUnsignedByte",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testInteger",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testPositiveInteger",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testNegativeInteger",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testNonNegativeInteger",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testNonPositiveInteger",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testInt",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testUnsignedInt",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testLong",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testUnsignedLong",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testShort",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testUnsignedShort",
                    "type": int,
                    "namespace": "",
                    "fraction_digits": 0,
                },
                {
                    "name": "testDecimal",
                    "type": Decimal,
                    "namespace": "",
                    "fraction_digits": 5,
                },
            ),
        }
    )
