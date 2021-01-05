from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Element:
    class Meta:
        namespace = "ElemDecl/valueConstraint"

    value: str = field(
        init=False,
        default="1.0E-2",
        metadata={
            "required": True,
            "pattern": r"...[Ee]..",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    element: Optional[str] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Element",
            "required": True,
            "pattern": r"...[Ee]..",
        }
    )
