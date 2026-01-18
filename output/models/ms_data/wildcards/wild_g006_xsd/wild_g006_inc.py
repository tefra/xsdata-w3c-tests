from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://xsdtesting"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
