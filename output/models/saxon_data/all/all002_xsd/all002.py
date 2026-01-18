from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class C1:
    class Meta:
        name = "C"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class D1:
    class Meta:
        name = "D"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class C2:
    class Meta:
        name = "c"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class D2:
    class Meta:
        name = "d"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    a: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    b: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    c_or_c: list[C1 | C2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "C",
                    "type": C1,
                },
                {
                    "name": "c",
                    "type": C2,
                },
            ),
        },
    )
    d_or_d: None | D1 | D2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "D",
                    "type": D1,
                },
                {
                    "name": "d",
                    "type": D2,
                },
            ),
        },
    )
