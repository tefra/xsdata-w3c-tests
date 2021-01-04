from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "a"


class Type(Enum):
    X = QName("{a}x")


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "a"

    value: Optional[Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
