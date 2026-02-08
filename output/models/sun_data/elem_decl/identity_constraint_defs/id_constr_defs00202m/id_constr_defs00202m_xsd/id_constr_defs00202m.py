from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    person: list[Root.Person] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Person:
        value: str = field(default="")
        birthday: None | XmlDate = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
