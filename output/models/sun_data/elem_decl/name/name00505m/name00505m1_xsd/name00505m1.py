from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class Global1:
    class Meta:
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Global2:
    class Meta:
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
