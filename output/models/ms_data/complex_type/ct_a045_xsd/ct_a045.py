from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Xmlns:
    class Meta:
        name = "xmlns"

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
class Root(Xmlns):
    class Meta:
        name = "root"
