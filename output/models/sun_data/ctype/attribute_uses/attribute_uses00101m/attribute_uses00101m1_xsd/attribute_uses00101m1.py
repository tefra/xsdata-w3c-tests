from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "attributeUses"


@dataclass
class A1:
    class Meta:
        name = "A"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    attr1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    attr2: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "attributeUses"
