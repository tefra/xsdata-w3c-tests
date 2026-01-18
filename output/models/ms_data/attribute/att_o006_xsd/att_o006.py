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

    @dataclass(kw_only=True)
    class Elem:
        att: int = field(
            init=False,
            default=123,
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
            },
        )
