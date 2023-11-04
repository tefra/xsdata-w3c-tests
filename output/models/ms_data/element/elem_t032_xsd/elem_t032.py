from dataclasses import dataclass, field
from typing import List, Optional, Union


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
class Test:
    class Meta:
        name = "test"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 0,
            "max_inclusive": 10,
        }
    )


@dataclass
class Test2:
    class Meta:
        name = "test2"

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
class Test3(Ca):
    class Meta:
        name = "test3"


@dataclass
class Root:
    class Meta:
        name = "root"

    s_a_or_test: Optional[Union[SA, int]] = field(
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
                    "type": int,
                    "min_exclusive": 0,
                    "max_inclusive": 10,
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
    test3: Optional[Test3] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
