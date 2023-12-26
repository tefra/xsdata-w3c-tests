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
        },
    )


@dataclass
class Uidtype:
    class Meta:
        name = "uidtype"

    hid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    iid: Optional["Uidtype.Iid"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class Iid:
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

    uid: List[Uidtype] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    kid: List[Kid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
