from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "targetNS"


class PictureType(Enum):
    TEST_PNG = QName("{tck_test}png")


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "targetNS"

    value: Optional[str] = field(
        default=None,
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
