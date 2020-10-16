from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar open_com_element:
    """
    class Meta:
        name = "doc"

    open_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "mixed": True,
        }
    )
