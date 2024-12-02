from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://id054.ly/"


@dataclass
class EmpType:
    class Meta:
        name = "empType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    nr: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    manager: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://id054.ly/"

    emp: list[EmpType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
