from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    version: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "element",
                    "type": str,
                },
            ),
        },
    )
