from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Base:
    annotation: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    element_or_any: list[Base.Element | Base.AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "element",
                    "type": ForwardRef("Base.Element"),
                    "namespace": "",
                },
                {
                    "name": "any",
                    "type": ForwardRef("Base.AnyType"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Element:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class AnyType:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class Derived(Base):
    any: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | Derived = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
