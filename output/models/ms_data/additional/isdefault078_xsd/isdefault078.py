from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    space: Optional["Root.Space"] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )

    class Space(Enum):
        DEFAULT = "default"
        PRESERVE = "preserve"
