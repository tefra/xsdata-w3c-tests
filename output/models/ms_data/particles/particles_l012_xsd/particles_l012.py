from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Mixed:
    class Meta:
        name = "mixed"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class B:
    c1_or_c2: None | Mixed | object = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": Mixed,
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": object,
                    "namespace": "",
                },
            ),
        },
    )
    d1_or_d2: None | B.D1 | B.D2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "d1",
                    "type": ForwardRef("B.D1"),
                    "namespace": "",
                },
                {
                    "name": "d2",
                    "type": ForwardRef("B.D2"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class D1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class D2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class NotMixed(Mixed):
    class Meta:
        name = "not_mixed"

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    foo: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class R(B):
    c2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    d2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    c1: NotMixed = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    d1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | R = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
