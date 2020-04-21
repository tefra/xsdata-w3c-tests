from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class MyType:
    """
    :ivar x:
    :ivar y:
    """
    class Meta:
        name = "myType"

    x: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=2
        )
    )
    y: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class NsAAft:
    """
    :ivar x:
    :ivar y:
    """
    class Meta:
        name = "ns-a-aft"

    x: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=10
        )
    )
    y: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Abc(MyType):
    class Meta:
        name = "abc"
        namespace = "ns-a"


@dataclass
class Foo:
    """
    :ivar a:
    :ivar abc:
    :ivar aft:
    """
    class Meta:
        name = "foo"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    abc: Optional[Abc] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a"
        )
    )
    aft: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a"
        )
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
        namespace = "ns-a"
