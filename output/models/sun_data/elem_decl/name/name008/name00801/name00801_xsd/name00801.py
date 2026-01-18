from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class AA:
    class Meta:
        name = "a--a"
        namespace = "ElemDecl/name"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BB:
    class Meta:
        name = "b..b"
        namespace = "ElemDecl/name"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CC:
    class Meta:
        name = "c__c"
        namespace = "ElemDecl/name"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DD:
    class Meta:
        name = "d··d"
        namespace = "ElemDecl/name"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class EE:
    class Meta:
        name = "e··e"
        namespace = "ElemDecl/name"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FF:
    class Meta:
        name = "f۝۝f"
        namespace = "ElemDecl/name"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GG:
    class Meta:
        name = "g۞۞g"
        namespace = "ElemDecl/name"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    a_a: AA = field(
        metadata={
            "name": "a--a",
            "type": "Element",
            "required": True,
        }
    )
    b_b: BB = field(
        metadata={
            "name": "b..b",
            "type": "Element",
            "required": True,
        }
    )
    c_c: CC = field(
        metadata={
            "name": "c__c",
            "type": "Element",
            "required": True,
        }
    )
    d_d: DD = field(
        metadata={
            "name": "d··d",
            "type": "Element",
            "required": True,
        }
    )
    e_e: EE = field(
        metadata={
            "name": "e··e",
            "type": "Element",
            "required": True,
        }
    )
    f_f: FF = field(
        metadata={
            "name": "f۝۝f",
            "type": "Element",
            "required": True,
        }
    )
    g_g: GG = field(
        metadata={
            "name": "g۞۞g",
            "type": "Element",
            "required": True,
        }
    )
