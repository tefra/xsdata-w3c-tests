from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComType:
    class Meta:
        name = "comType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root(ComType):
    class Meta:
        name = "root"
