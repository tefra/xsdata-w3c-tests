from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: bool = field()


@dataclass(kw_only=True)
class Root2:
    class Meta:
        name = "root2"
        namespace = "ElemDecl/name"

    value: str = field(init=False, default="No")
