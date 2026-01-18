from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    list_of_ids_attr: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    idref_attr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
