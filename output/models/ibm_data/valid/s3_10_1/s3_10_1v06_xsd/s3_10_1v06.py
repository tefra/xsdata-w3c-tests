from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "a"

    value: int = field()


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"
        namespace = "a"

    value: int = field()


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"
        namespace = "a"

    value: int = field()


@dataclass(kw_only=True)
class D:
    class Meta:
        name = "d"
        namespace = "a"

    value: int = field()


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    d_or_b: None | D | B = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "d",
                    "type": D,
                    "namespace": "a",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "a",
                },
            ),
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    c: C = field(
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )


@dataclass(kw_only=True)
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
