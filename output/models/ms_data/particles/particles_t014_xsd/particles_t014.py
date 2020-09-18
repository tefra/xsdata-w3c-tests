from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Foo:
    """
    :ivar foo:
    :ivar att:
    """
    class Meta:
        name = "foo"

    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    att: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Bar(Foo):
    """
    :ivar att1:
    """
    class Meta:
        name = "bar"

    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class B:
    """
    :ivar c1:
    :ivar c2:
    :ivar c3:
    :ivar foo:
    """
    c1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    c2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    c3: List[Bar] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class R:
    """
    :ivar c1:
    :ivar c2:
    :ivar c3:
    :ivar foo:
    """
    c1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    c2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    c3: List[Bar] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
