from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar list_of_ids_element:
    :ivar idref_element:
    :ivar idref_attr:
    """
    class Meta:
        name = "root"

    list_of_ids_element: List[List[str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "tokens": True,
        }
    )
    idref_element: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    idref_attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
