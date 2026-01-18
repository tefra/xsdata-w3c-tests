from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from xml.etree.ElementTree import QName

__NAMESPACE__ = "targetNS"


class PictureType(Enum):
    TEST_PNG = QName("{tck_test}png")


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class Picture:
    type_value: None | PictureType = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
