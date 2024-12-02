from dataclasses import dataclass, field
from typing import Optional


@dataclass
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
    idref_element: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    idref_attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
