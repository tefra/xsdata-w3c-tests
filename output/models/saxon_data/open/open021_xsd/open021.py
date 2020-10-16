from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar open_com_element:
    """
    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
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
    open_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "mixed": True,
        }
    )


@dataclass
class R:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar open_com_element:
    """
    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
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
    open_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "mixed": True,
        }
    )


@dataclass
class Doc(R):
    class Meta:
        name = "doc"
