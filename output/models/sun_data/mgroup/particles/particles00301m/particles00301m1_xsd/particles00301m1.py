from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "particles"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    id: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
