from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Triangular:
    a: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    kind: str = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class Quadrilateral(Triangular):
    d: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
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
