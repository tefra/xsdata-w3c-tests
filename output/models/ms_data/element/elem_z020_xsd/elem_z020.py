from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class E1:
    """
    :ivar value:
    """
    class Meta:
        name = "e1"
        namespace = "foo"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Foo:
    """
    :ivar value:
    """
    class Meta:
        name = "foo"
        namespace = "foo"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class B:
    """
    :ivar foo_foo:
    :ivar e1:
    :ivar foo:
    """
    foo_foo: List[Foo] = field(
        default_factory=list,
        metadata=dict(
            name="foo",
            type="Element",
            namespace="foo",
            min_occurs=0,
            max_occurs=1000
        )
    )
    e1: List[E1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="foo",
            min_occurs=0,
            max_occurs=1000
        )
    )
    foo: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=1000
        )
    )


@dataclass
class Root(B):
    class Meta:
        name = "root"
        namespace = "foo"
