from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "main"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "main"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "main"

    target_namespace_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "process_contents": "skip",
        }
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "main"

    foo_bar_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo bar",
            "process_contents": "skip",
        }
    )


@dataclass
class D:
    class Meta:
        name = "d"
        namespace = "main"

    target_namespace_foo_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace foo",
            "process_contents": "skip",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "main"

    a: List[A] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        }
    )
    b: List[B] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        }
    )
    c: List[C] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        }
    )
    d: List[D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        }
    )
