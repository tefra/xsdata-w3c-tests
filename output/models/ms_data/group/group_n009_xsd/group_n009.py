from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elem:
    class Meta:
        name = "elem"

    a1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 3,
        }
    )
    a2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 3,
        }
    )
    a3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 3,
        }
    )
    a4: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 3,
        }
    )
    a5: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 3,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
