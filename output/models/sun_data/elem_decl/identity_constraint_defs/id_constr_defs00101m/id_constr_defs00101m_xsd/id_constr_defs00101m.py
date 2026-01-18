from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    sernum: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
        },
    )
