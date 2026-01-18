from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.identity_constraint.id_h027_xsd.id_h027_imp import (
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
class Uidtype:
    class Meta:
        name = "uidtype"

    iid: Iid = field(
        metadata={
            "type": "Element",
            "namespace": "importNS",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    uid: list[Uidtype] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    kid: list[Kid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
