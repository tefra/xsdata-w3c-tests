from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar e:
    :ivar f:
    :ivar type:
    """
    e: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 5,
        }
    )
    f: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 5,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        }
    )


@dataclass
class R:
    """
    :ivar e:
    :ivar f:
    :ivar type:
    """
    e: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    f: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        }
    )


@dataclass
class Root(B):
    class Meta:
        name = "root"
