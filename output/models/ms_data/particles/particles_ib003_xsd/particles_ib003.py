from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Bar:
    """
    :ivar any_element:
    """
    class Meta:
        name = "bar"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Base:
    """
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "base"

    foo: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=6
        )
    )
    bar: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Foo:
    """
    :ivar any_element:
    """
    class Meta:
        name = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "doc"

    foo: List[Foo] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    bar: Optional[Bar] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
