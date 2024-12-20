from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
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
    idref_element: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
