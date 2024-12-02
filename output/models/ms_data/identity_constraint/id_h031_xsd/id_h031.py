from dataclasses import dataclass, field
from typing import Optional

from output.models.ms_data.identity_constraint.id_h031_xsd.id_h031_imp import (
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
class Uidtype:
    class Meta:
        name = "uidtype"

    iid: Optional[Iid] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "importNS",
            "required": True,
        },
    )


@dataclass
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
