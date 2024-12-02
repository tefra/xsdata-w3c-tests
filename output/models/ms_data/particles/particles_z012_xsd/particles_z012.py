from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class E2:
    class Meta:
        namespace = "http://xsdtesting"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


class MyType10Value(Enum):
    X = "x"
    Y = "y"


@dataclass
class Ct1:
    class Meta:
        name = "CT1"

    att1: Optional[Union[bool, float, int, MyType10Value]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass
class E1:
    class Meta:
        namespace = "http://xsdtesting"

    value: Optional[Union[bool, float, int, MyType10Value]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Ct2(Ct1):
    class Meta:
        name = "CT2"


@dataclass
class E3(Ct2):
    class Meta:
        namespace = "http://xsdtesting"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    e2_or_e1_or_e3: list[Union[E2, E1, E3]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "E2",
                    "type": E2,
                },
                {
                    "name": "E1",
                    "type": E1,
                },
                {
                    "name": "E3",
                    "type": E3,
                },
            ),
        },
    )
