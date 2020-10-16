from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar local_com_element:
    """
    class Meta:
        name = "doc"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    local_com_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://local.com/",
            "required": True,
        }
    )
