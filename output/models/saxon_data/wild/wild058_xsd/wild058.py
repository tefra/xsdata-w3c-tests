from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )
