from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bar: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
