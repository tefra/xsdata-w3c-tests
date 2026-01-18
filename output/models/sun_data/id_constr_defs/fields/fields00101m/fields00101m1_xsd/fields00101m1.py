from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "IdConstrDefs/fields"


@dataclass(kw_only=True)
class People:
    class Meta:
        name = "people"
        namespace = "IdConstrDefs/fields"

    person: list[People.Person] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Person:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        parent: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        birthday: None | XmlDate = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
