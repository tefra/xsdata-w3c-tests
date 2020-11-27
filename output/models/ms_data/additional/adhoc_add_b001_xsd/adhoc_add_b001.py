from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class MyType:
    class Meta:
        name = "myType"

    x: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
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
class Abc(MyType):
    class Meta:
        name = "abc"
        namespace = "ns-a"


@dataclass
class Aft(NsAAft):
    class Meta:
        name = "aft"
        namespace = "ns-a"


@dataclass
class Foo:
    class Meta:
        name = "foo"

    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    abc: Optional[Abc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
        }
    )
    aft: Optional[Aft] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
        }
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
        namespace = "ns-a"
