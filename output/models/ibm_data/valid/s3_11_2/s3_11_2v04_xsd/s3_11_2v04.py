from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class Keyname:
    class Meta:
        name = "keyname"

    numid: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numid",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    numname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numname",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    number: List[Keyname] = field(
        default_factory=list,
        metadata={
            "name": "Number",
            "type": "Element",
            "min_occurs": 1,
        },
    )
