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
class Uidtype:
    class Meta:
        name = "uidtype"

    hid: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    iid: Uidtype.Iid = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Iid:
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
