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
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
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
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        }
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
        metadata={
            "type": "Wildcard",
            "namespace": "foo bar",
        }
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
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace foo",
        }
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
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    b: List[B] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    c: List[C] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    d: List[D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
