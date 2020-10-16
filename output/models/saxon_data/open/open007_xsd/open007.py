from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar open_com_element:
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "doc"

    open_com_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "required": True,
        }
    )
    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 5,
            "max_occurs": 10,
        }
    )
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
