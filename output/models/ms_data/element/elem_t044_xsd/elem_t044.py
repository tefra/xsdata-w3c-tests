from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List, Optional, Union


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
        },
    )
    y: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Sa:
    class Meta:
        name = "sa"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Test4:
    class Meta:
        name = "test4"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
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
        },
    )


@dataclass
class RCa(Ca):
    class Meta:
        name = "R-CA"

    y: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Test:
    class Meta:
        name = "test"

    value: Optional[A] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Test2:
    class Meta:
        name = "test2"

    value: Optional[A] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Test3:
    class Meta:
        name = "test3"

    value: Optional[A] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    sa_or_test: Optional[Union[Sa, Test]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "sa",
                    "type": Sa,
                },
                {
                    "name": "test",
                    "type": Test,
                },
            ),
        },
    )
    test2: Optional[Test2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    test3: Optional[Test3] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    test4: Optional[Test4] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
