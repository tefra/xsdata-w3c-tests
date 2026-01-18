from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    ca1: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ca2: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    aga1: object = field(
        default="abc",
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
    aga2: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ga2: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | AttRef = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ga1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
