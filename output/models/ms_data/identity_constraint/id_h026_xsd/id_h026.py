from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Kid:
    class Meta:
        name = "kid"
        namespace = "myNS.tempuri.org"

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

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    uid: list[Uidtype] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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
