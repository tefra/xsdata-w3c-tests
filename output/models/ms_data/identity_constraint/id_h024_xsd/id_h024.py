from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Kid:
    class Meta:
        name = "kid"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class UidType:
    class Meta:
        name = "uidType"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
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

    uid2_or_uid: list[Union[Uid2, Uid]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "uid2",
                    "type": Uid2,
                },
                {
                    "name": "uid",
                    "type": Uid,
                },
            ),
        },
    )
    kid: list[Kid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
