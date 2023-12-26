from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://id050.ly/"


@dataclass
class EmpType:
    class Meta:
        name = "empType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://id050.ly/",
            "required": True,
        },
    )
    nr: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://id050.ly/",
            "required": True,
        },
    )
    manager: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://id050.ly/",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://id050.ly/"

    emp: List[EmpType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
