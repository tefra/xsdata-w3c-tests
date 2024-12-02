from dataclasses import dataclass, field
from typing import Any, Optional, Union

__NAMESPACE__ = "ns-a"


@dataclass
class NsAAft:
    class Meta:
        name = "ns-a-aft"

    x: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 10,
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
class Aft(NsAAft):
    class Meta:
        name = "aft"
        namespace = "ns-a"


@dataclass
class MyType(NsAAft):
    class Meta:
        name = "myType"

    y: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Abc(MyType):
    class Meta:
        name = "abc"
        namespace = "ns-a"


@dataclass
class Foo:
    class Meta:
        name = "foo"

    a_or_abc: Optional[Union[str, Abc]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "abc",
                    "type": Abc,
                    "namespace": "ns-a",
                },
            ),
        },
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
        namespace = "ns-a"
