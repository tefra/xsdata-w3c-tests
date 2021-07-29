from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "name"


class PictureType(Enum):
    PNG = QName("{name}png")


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Picture:
    type: Optional[PictureType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
