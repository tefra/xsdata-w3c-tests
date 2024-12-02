from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    element: list["Root.Element"] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Element:
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "ID",
                "type": "Attribute",
            },
        )
        idref: Optional[str] = field(
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
