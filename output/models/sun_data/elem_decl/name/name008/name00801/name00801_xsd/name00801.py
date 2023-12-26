from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class AA:
    class Meta:
        name = "a--a"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class BB:
    class Meta:
        name = "b..b"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class CC:
    class Meta:
        name = "c__c"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class DD:
    class Meta:
        name = "d··d"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class EE:
    class Meta:
        name = "e··e"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class FF:
    class Meta:
        name = "f۝۝f"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class GG:
    class Meta:
        name = "g۞۞g"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    a_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "a--a",
            "type": "Element",
            "required": True,
        },
    )
    b_b: Optional[int] = field(
        default=None,
        metadata={
            "name": "b..b",
            "type": "Element",
            "required": True,
        },
    )
    c_c: Optional[int] = field(
        default=None,
        metadata={
            "name": "c__c",
            "type": "Element",
            "required": True,
        },
    )
    d_d: Optional[int] = field(
        default=None,
        metadata={
            "name": "d··d",
            "type": "Element",
            "required": True,
        },
    )
    e_e: Optional[int] = field(
        default=None,
        metadata={
            "name": "e··e",
            "type": "Element",
            "required": True,
        },
    )
    f_f: Optional[int] = field(
        default=None,
        metadata={
            "name": "f۝۝f",
            "type": "Element",
            "required": True,
        },
    )
    g_g: Optional[int] = field(
        default=None,
        metadata={
            "name": "g۞۞g",
            "type": "Element",
            "required": True,
        },
    )
