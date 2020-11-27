from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Kid:
    class Meta:
        name = "kid"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class UidType:
    class Meta:
        name = "uidType"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Uid(UidType):
    class Meta:
        name = "uid"


@dataclass
class Uid2(UidType):
    class Meta:
        name = "uid2"


@dataclass
class Root:
    class Meta:
        name = "root"

    uid2: List[Uid2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    uid: List[Uid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    kid: List[Kid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
