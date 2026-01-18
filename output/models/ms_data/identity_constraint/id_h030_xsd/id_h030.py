from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass(kw_only=True)
class Kid:
    class Meta:
        name = "kid"
        namespace = "myNS.tempuri.org"

    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        },
    )


@dataclass(kw_only=True)
class Uidtype:
    class Meta:
        name = "uidtype"

    iid: Uidtype.Iid = field(
        metadata={
            "type": "Element",
            "namespace": "myNS.tempuri.org",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Iid:
        val: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "myNS.tempuri.org",
            },
        )


@dataclass(kw_only=True)
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
