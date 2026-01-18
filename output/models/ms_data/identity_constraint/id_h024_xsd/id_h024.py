from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Kid:
    class Meta:
        name = "kid"

    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class UidType:
    class Meta:
        name = "uidType"

    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Uid(UidType):
    class Meta:
        name = "uid"


@dataclass(kw_only=True)
class Uid2(UidType):
    class Meta:
        name = "uid2"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    uid2_or_uid: list[Uid2 | Uid] = field(
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
