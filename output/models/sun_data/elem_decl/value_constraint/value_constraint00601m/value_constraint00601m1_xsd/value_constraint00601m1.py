from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    value: str = field(init=False, default="1.0e-2")
