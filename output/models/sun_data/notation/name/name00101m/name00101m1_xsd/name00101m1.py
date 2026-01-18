from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from xml.etree.ElementTree import QName

__NAMESPACE__ = "name"


class PictureType(Enum):
    PNG = QName("{name}png")


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "name"

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
