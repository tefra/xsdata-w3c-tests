from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    idref_element: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    union_of_ids_attr1: None | int | bool | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    union_of_ids_attr2: None | int | bool | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    union_of_ids_attr3: None | int | bool | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
