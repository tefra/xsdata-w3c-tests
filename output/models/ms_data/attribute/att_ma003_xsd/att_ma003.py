from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | Doc.Elem = field(
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

    @dataclass(kw_only=True)
    class Elem:
        ga1: None | int = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
            },
        )
        ga2: None | int = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
            },
        )
