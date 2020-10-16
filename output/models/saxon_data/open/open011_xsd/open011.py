from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar open_com_element:
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
