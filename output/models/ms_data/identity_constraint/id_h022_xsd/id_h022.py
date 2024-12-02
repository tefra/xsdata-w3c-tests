from dataclasses import dataclass, field
from typing import Optional

from output.models.ms_data.identity_constraint.id_h022_xsd.id_h022_imp import (
    Iid,
)


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
class Uid:
    class Meta:
        name = "uid"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
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
