from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    e: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 5,
        },
    )
    f: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 5,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        },
    )


@dataclass
class R(B):
    pass


@dataclass
class Root(B):
    class Meta:
        name = "root"
