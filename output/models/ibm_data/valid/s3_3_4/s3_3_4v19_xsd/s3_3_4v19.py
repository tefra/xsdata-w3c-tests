from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    union_of_ids_element: list[int | bool | str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    idref_attr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
