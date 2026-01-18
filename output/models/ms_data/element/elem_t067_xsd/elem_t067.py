from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class A(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass(kw_only=True)
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
    y: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


class RA(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class Sa3:
    class Meta:
        name = "sa3"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EA:
    class Meta:
        name = "E-A"

    value: A = field(
        metadata={
            "required": True,
        }
    )
    att: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ECa(Ca):
    class Meta:
        name = "E-CA"

    z: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
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
    x: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class Sa1:
    class Meta:
        name = "sa1"

    value: RA = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test1:
    class Meta:
        name = "test1"

    value: A = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test2:
    class Meta:
        name = "test2"

    value: A = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test3:
    class Meta:
        name = "test3"

    value: A = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test4(Ca):
    class Meta:
        name = "test4"


@dataclass(kw_only=True)
class Test5(Ca):
    class Meta:
        name = "test5"


@dataclass(kw_only=True)
class Sa2(EA):
    class Meta:
        name = "sa2"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    choice: list[Sa3 | Sa2 | Sa1 | Test1] = field(
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
    test2: None | Test2 = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    test3: None | Test3 = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    test4: None | Test4 = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    test5: None | Test5 = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
