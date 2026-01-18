from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    target_namespace_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


@dataclass(kw_only=True)
class E1:
    class Meta:
        name = "e1"
        namespace = "http://xsdtesting"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class R(B):
    target_namespace_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    e1: E1 = field(
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "required": True,
        }
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
