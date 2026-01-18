from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    element: list[Root.Element] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass(kw_only=True)
    class Element:
        id: None | str = field(
            default=None,
            metadata={
                "name": "ID",
                "type": "Attribute",
            },
        )
        idref: None | str = field(
            default=None,
            metadata={
                "name": "IDREF",
                "type": "Attribute",
            },
        )
        idrefs: list[str] = field(
            default_factory=list,
            metadata={
                "name": "IDREFS",
                "type": "Attribute",
                "tokens": True,
            },
        )
