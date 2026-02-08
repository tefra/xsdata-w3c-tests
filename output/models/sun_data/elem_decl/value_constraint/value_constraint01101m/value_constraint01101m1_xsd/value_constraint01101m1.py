from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    element: str = field(
        init=False,
        default="0",
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
            "max_inclusive": "0",
        },
    )
