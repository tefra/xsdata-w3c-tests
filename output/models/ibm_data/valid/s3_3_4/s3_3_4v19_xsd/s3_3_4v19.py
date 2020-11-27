from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    union_of_ids_element: List[Union[int, bool, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    idref_attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
