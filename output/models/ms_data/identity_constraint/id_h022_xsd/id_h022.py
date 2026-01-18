from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.identity_constraint.id_h022_xsd.id_h022_imp import (
    Iid,
)


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
class Uid:
    class Meta:
        name = "uid"

    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    uid: list[Uid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    iid: list[Iid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "importNS",
        },
    )
    kid: list[Kid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
