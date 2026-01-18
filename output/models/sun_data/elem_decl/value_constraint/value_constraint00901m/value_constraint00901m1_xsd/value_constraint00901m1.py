from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    value: object = field(
        init=False,
        default="alpha beta",
        metadata={
            "required": True,
        },
    )
