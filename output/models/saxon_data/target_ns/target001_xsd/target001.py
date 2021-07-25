from dataclasses import dataclass, field
from typing import Optional


@dataclass
class B:
    target001_com_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.target001.com/",
        }
    )


@dataclass
class R(B):
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
