from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "foo"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"
        namespace = "foo"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"
        namespace = "foo"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    mixed_or_element_only: list[Root.Mixed | Root.ElementOnly] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "mixed",
                    "type": ForwardRef("Root.Mixed"),
                },
                {
                    "name": "elementOnly",
                    "type": ForwardRef("Root.ElementOnly"),
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Mixed:
        content: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
                "choices": (
                    {
                        "name": "a",
                        "type": A,
                    },
                    {
                        "name": "b",
                        "type": B,
                    },
                    {
                        "name": "c",
                        "type": C,
                    },
                ),
            },
        )

    @dataclass(kw_only=True)
    class ElementOnly:
        a_or_b_or_c: list[A | B | C] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "a",
                        "type": A,
                    },
                    {
                        "name": "b",
                        "type": B,
                    },
                    {
                        "name": "c",
                        "type": C,
                    },
                ),
            },
        )
