from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://id050.ly/"


@dataclass(kw_only=True)
class EmpType:
    class Meta:
        name = "empType"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://id050.ly/",
            "required": True,
        }
    )
    nr: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://id050.ly/",
            "required": True,
        }
    )
    manager: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://id050.ly/",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://id050.ly/"

    emp: list[EmpType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
