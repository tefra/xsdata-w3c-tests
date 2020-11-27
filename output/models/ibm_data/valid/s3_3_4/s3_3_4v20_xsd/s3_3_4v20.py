from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    idref_element: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    union_of_ids_attr1: Optional[Union[int, bool, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    union_of_ids_attr2: Optional[Union[int, bool, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    union_of_ids_attr3: Optional[Union[int, bool, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
