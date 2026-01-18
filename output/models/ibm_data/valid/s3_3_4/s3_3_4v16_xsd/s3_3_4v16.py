from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    idref_element: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    list_of_ids_attr: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
