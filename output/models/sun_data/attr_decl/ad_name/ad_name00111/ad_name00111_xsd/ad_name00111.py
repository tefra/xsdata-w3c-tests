from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    a_a: None | int = field(
        default=None,
        metadata={
            "name": "a--a",
            "type": "Attribute",
        },
    )
    b_b: None | int = field(
        default=None,
        metadata={
            "name": "b..b",
            "type": "Attribute",
        },
    )
    c_c: None | int = field(
        default=None,
        metadata={
            "name": "c__c",
            "type": "Attribute",
        },
    )
    d_d: None | int = field(
        default=None,
        metadata={
            "name": "d··d",
            "type": "Attribute",
        },
    )
    e_e: None | int = field(
        default=None,
        metadata={
            "name": "e··e",
            "type": "Attribute",
        },
    )
    f_f: None | int = field(
        default=None,
        metadata={
            "name": "f۝۝f",
            "type": "Attribute",
        },
    )
    g_g: None | int = field(
        default=None,
        metadata={
            "name": "g۞۞g",
            "type": "Attribute",
        },
    )
