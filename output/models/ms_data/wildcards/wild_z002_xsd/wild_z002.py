from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "main"


@dataclass
class A:
    """
    :ivar any_element:
    """
    class Meta:
        name = "a"
        namespace = "main"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class B:
    """
    :ivar target_namespace_element:
    """
    class Meta:
        name = "b"
        namespace = "main"

    target_namespace_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##targetNamespace",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class C:
    """
    :ivar foo_bar_element:
    """
    class Meta:
        name = "c"
        namespace = "main"

    foo_bar_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="foo bar",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class D:
    """
    :ivar target_namespace_foo_element:
    """
    class Meta:
        name = "d"
        namespace = "main"

    target_namespace_foo_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##targetNamespace foo",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
    """
    class Meta:
        name = "root"
        namespace = "main"

    a: List[A] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    b: List[B] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    c: List[C] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    d: List[D] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
