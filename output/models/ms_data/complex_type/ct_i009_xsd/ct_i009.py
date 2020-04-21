from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar my_ele1:
    :ivar my_ele2:
    :ivar my_ele3:
    """
    class Meta:
        name = "foo"

    my_ele1: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myEle1",
            type="Element",
            namespace=""
        )
    )
    my_ele2: Optional[int] = field(
        default=None,
        metadata=dict(
            name="myEle2",
            type="Element",
            namespace=""
        )
    )
    my_ele3: Optional[int] = field(
        default=None,
        metadata=dict(
            name="myEle3",
            type="Element",
            namespace=""
        )
    )


@dataclass
class FooType(Foo):
    """
    :ivar my_ele4:
    """
    class Meta:
        name = "fooType"

    my_ele4: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myEle4",
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
