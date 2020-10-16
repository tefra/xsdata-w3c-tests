from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Alpha:
    """
    :ivar open_com_element:
    """
    class Meta:
        name = "alpha"

    open_com_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "required": True,
        }
    )


@dataclass
class Doc:
    """
    :ivar a:
    :ivar b:
    :ivar open_com_element:
    """
    class Meta:
        name = "doc"

    a: Optional[Alpha] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    open_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "mixed": True,
        }
    )
