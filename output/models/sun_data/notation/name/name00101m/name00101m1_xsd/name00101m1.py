from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "name"


@dataclass
class Picture:
    type: Optional["Picture.Type"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Type(Enum):
        PNG = QName("{name}png")


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "name"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
