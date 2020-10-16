from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Eden:
    """
    :ivar a:
    :ivar any_element:
    """
    class Meta:
        name = "eden"

    a: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
