from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class Type:
    class Meta:
        name = "_-."
        namespace = "ElemDecl/name"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Type0:
    class Meta:
        name = "_-0."
        namespace = "ElemDecl/name"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    low_line_hyphen_minus_full_stop: Type = field(
        metadata={
            "name": "_-.",
            "type": "Element",
            "required": True,
        }
    )
    value_0: Type0 = field(
        metadata={
            "name": "_-0.",
            "type": "Element",
            "required": True,
        }
    )
