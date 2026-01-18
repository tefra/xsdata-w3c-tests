from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Computer:
    class Meta:
        name = "computer"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
