from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/scope"


@dataclass(kw_only=True)
class Global:
    class Meta:
        namespace = "ElemDecl/scope"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/scope"

    global_value: Global = field(
        metadata={
            "name": "Global",
            "type": "Element",
            "required": True,
        }
    )
    local: None | object = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        },
    )
