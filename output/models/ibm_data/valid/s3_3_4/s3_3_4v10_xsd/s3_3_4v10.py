from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    list_of_ids: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "tokens": True,
        },
    )
    idref: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
