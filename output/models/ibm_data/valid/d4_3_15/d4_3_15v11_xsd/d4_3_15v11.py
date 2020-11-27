from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RootType:
    class Meta:
        name = "rootType"

    ele: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
