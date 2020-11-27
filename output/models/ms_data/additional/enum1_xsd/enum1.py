from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class EnumType(Enum):
    VALUE = "Ѐvalue"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    foo: Optional[EnumType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    att: Optional[EnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
