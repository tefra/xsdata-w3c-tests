from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "IdConstrDefs/fields"


@dataclass
class People:
    class Meta:
        name = "people"
        namespace = "IdConstrDefs/fields"

    person: List["People.Person"] = field(
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
        parent: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        birthday: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
