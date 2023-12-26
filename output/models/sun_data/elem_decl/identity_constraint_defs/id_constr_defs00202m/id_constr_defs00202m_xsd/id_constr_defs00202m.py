from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    person: List["Root.Person"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Person:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        birthday: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
