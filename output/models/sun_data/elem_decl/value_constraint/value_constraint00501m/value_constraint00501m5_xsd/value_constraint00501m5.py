from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass(kw_only=True)
class Element:
    class Meta:
        namespace = "ElemDecl/valueConstraint"

    value: str = field(
        default="1.0e-2",
        metadata={
            "required": True,
            "pattern": r"...[Ee]..",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    element: Element = field(
        metadata={
            "name": "Element",
            "type": "Element",
            "required": True,
        }
    )
