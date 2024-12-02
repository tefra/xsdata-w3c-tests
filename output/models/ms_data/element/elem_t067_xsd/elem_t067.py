from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional, Union


class A(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass
class Ca:
    class Meta:
        name = "CA"

    x: list[object] = field(
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


class RA(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class Sa3:
    class Meta:
        name = "sa3"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class EA:
    class Meta:
        name = "E-A"

    value: Optional[A] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Sa1:
    class Meta:
        name = "sa1"

    value: Optional[RA] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Test1:
    class Meta:
        name = "test1"

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
class Test4(Ca):
    class Meta:
        name = "test4"


@dataclass
class Test5(Ca):
    class Meta:
        name = "test5"


@dataclass
class Sa2(EA):
    class Meta:
        name = "sa2"


@dataclass
class Root:
    class Meta:
        name = "root"

    choice: list[Union[Sa3, Sa2, Sa1, Test1]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "sa3",
                    "type": Sa3,
                    "max_occurs": 5,
                },
                {
                    "name": "sa2",
                    "type": Sa2,
                    "max_occurs": 5,
                },
                {
                    "name": "sa1",
                    "type": Sa1,
                    "max_occurs": 5,
                },
                {
                    "name": "test1",
                    "type": Test1,
                    "max_occurs": 5,
                },
            ),
            "max_occurs": 5,
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
    test5: Optional[Test5] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
