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

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Picture:
    type_value: Optional[PictureType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
