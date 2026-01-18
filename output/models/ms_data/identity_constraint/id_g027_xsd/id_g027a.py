from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "importNS"


@dataclass(kw_only=True)
class R:
    class Meta:
        name = "r"
        namespace = "importNS"

    val2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "importNS",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
