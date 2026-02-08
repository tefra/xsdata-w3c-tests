from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Shape1:
    class Meta:
        name = "Shape"

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
    d: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class Shape(Shape1):
    class Meta:
        name = "shape"
