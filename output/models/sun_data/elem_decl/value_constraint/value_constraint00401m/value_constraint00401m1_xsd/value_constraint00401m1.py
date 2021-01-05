from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class E:
    class Meta:
        namespace = "ElemDecl/valueConstraint"

    value: bool = field(
        default=True,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
