from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Type:
    local: None | object = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    local: None | object = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Global(Type):
    class Meta:
        namespace = "ElemDecl/typeDef"
