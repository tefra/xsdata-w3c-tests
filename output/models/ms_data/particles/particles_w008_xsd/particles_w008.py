from dataclasses import dataclass, field
from typing import Any, List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 3,
        },
    )
    e3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 3,
        },
    )


@dataclass
class R(B):
    e2: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    e3: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
