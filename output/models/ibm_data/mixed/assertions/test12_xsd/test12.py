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
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Shape(Shape1):
    class Meta:
        name = "shape"
