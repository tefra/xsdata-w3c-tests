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
        att: list[str] = field(
            init=False,
            default_factory=lambda: [
                "A",
                "B",
            ],
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
                "tokens": True,
            },
        )
