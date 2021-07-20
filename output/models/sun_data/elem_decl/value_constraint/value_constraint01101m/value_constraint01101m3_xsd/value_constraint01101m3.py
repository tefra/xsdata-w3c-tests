from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    element: Optional[float] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
            "max_inclusive": 0.0,
        }
    )
