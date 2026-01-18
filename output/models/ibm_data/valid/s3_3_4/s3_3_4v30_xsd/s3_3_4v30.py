from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    list_of_ids_element: list[list[str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "tokens": True,
        },
    )
    idref_element: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
