from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "main"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "main"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"
        namespace = "main"

    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"
        namespace = "main"

    foo_bar_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo bar",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class D:
    class Meta:
        name = "d"
        namespace = "main"

    target_namespace_foo_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace foo",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "main"

    a: list[A] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    b: list[B] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    c: list[C] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    d: list[D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
