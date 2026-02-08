from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    list_of_ids_element: list[list[str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "tokens": True,
        },
    )
    idref_element: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    idref_attr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
