from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RootType:
    class Meta:
        name = "rootType"

    value: str = field(
        default="",
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
class Root(RootType):
    class Meta:
        name = "root"
