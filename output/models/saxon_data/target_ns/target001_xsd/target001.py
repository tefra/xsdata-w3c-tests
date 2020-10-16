from dataclasses import dataclass, field
from typing import Optional


@dataclass
class B:
    """
    :ivar target001_com_element:
    """
    target001_com_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.target001.com/",
            "required": True,
        }
    )


@dataclass
class R(B):
    """
    :ivar child:
    """
    child: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.target001.com/",
            "required": True,
        }
    )


@dataclass
class Parent(R):
    class Meta:
        name = "parent"
