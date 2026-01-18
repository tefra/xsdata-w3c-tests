from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "attributeUses"


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "A"

    value: int = field(
        metadata={
            "required": True,
        }
    )
    attr1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    attr2: XmlDate = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class A(A1):
    class Meta:
        name = "a"
        namespace = "attributeUses"
