from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "ns-a"


@dataclass
class NsAAft:
    class Meta:
        name = "ns-a-aft"

    x: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 10,
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
class MyType(NsAAft):
    class Meta:
        name = "myType"


@dataclass
class Abc(MyType):
    class Meta:
        name = "abc"
        namespace = "ns-a"


@dataclass
class Foo:
    class Meta:
        name = "foo"

    a_or_abc: Optional[Union[Abc, str]] = field(
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
        }
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
        namespace = "ns-a"
