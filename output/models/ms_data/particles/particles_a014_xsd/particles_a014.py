from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elem:
    """
    :ivar any_element:
    """
    class Meta:
        name = "elem"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "min_occurs": 2,
            "max_occurs": 1000000,
        }
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
