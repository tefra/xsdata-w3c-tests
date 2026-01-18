from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Triangular:
    a: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    c: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    kind: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Quadrilateral(Triangular):
    d: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Shapes:
    class Meta:
        name = "shapes"

    polygon: list[Triangular | Quadrilateral] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
