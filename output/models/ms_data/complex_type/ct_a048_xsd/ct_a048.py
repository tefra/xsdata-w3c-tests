from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Type1:
    class Meta:
        name = "_1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    attr_test: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        }
    )


@dataclass
class Root(Type1):
    class Meta:
        name = "root"
