from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Computer:
    class Meta:
        name = "computer"

    local_apple_com_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local http://apple.com/",
        },
    )
    local_orange_com_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local http://orange.com/",
        },
    )
