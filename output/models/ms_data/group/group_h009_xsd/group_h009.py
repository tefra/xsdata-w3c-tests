from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    """
    :ivar x1:
    :ivar x2:
    :ivar y1:
    :ivar y2:
    """
    x1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    x2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    y1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    y2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Elem:
    """
    :ivar x1:
    :ivar x2:
    :ivar y1:
    :ivar y2:
    """
    class Meta:
        name = "elem"

    x1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 999999999999999,
            "sequential": True,
        }
    )
    x2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 999999999999999,
            "sequential": True,
        }
    )
    y1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 999999999999999,
        }
    )
    y2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 999999999999999,
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
            "required": True,
        }
    )
