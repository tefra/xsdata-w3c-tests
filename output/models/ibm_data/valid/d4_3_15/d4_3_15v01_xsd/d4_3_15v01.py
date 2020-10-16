from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RootType:
    """
    :ivar ele:
    :ivar min:
    :ivar max:
    """
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
    min: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
