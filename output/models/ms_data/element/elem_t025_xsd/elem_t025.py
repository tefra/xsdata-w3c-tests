from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union


class A(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass
class Ca:
    class Meta:
        name = "CA"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
        }
    )
    y: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SA:
    class Meta:
        name = "s-a"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class ECa(Ca):
    class Meta:
        name = "E-CA"

    z: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RCa(Ca):
    class Meta:
        name = "R-CA"


@dataclass
class Test:
    class Meta:
        name = "test"

    value: Optional[A] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Test2(Ca):
    class Meta:
        name = "test2"


@dataclass
class Root:
    class Meta:
        name = "root"

    s_a_or_test: Optional[Union[SA, A]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "s-a",
                    "type": SA,
                },
                {
                    "name": "test",
                    "type": A,
                },
            ),
        }
    )
    test2: Optional[Test2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
