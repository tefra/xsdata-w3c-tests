from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class B:
    target001_com_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.target001.com/",
        },
    )


@dataclass
class R(B):
    target001_com_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    child: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.target001.com/",
            "required": True,
        },
    )


@dataclass
class Parent(R):
    class Meta:
        name = "parent"
