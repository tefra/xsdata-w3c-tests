from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar open_com_element:
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
    """
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
            "min_occurs": 1,
        }
    )
    b: Optional[int] = field(
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
    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class R(B):
    """
    :ivar any_element:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Doc(R):
    class Meta:
        name = "doc"
