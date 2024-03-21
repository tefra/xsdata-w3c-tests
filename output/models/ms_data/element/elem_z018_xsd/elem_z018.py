from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Signatures:
    class Meta:
        name = "signatures"

    w3_org_2000_09_xmldsig_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class Yyy:
    class Meta:
        name = "yyy"

    signatures: Optional[Signatures] = field(
        default=None,
        metadata={
            "wrapper": "zzz",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Zzz:
    class Meta:
        name = "zzz"

    signatures: Optional[Signatures] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Www:
    class Meta:
        name = "www"

    yyy: Optional[Yyy] = field(
        default=None,
        metadata={
            "wrapper": "xxx",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Xxx:
    class Meta:
        name = "xxx"

    zzz: Optional[Zzz] = field(
        default=None,
        metadata={
            "wrapper": "yyy",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ttt:
    class Meta:
        name = "ttt"

    www: Optional[Www] = field(
        default=None,
        metadata={
            "wrapper": "uuu",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Uuu:
    class Meta:
        name = "uuu"

    xxx: Optional[Xxx] = field(
        default=None,
        metadata={
            "wrapper": "www",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Rrr:
    class Meta:
        name = "rrr"

    ttt: Optional[Ttt] = field(
        default=None,
        metadata={
            "wrapper": "sss",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Sss:
    class Meta:
        name = "sss"

    uuu: Optional[Uuu] = field(
        default=None,
        metadata={
            "wrapper": "ttt",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ppp:
    class Meta:
        name = "ppp"

    rrr: Optional[Rrr] = field(
        default=None,
        metadata={
            "wrapper": "qqq",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Qqq:
    class Meta:
        name = "qqq"

    sss: Optional[Sss] = field(
        default=None,
        metadata={
            "wrapper": "rrr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Nnn:
    class Meta:
        name = "nnn"

    ppp: Optional[Ppp] = field(
        default=None,
        metadata={
            "wrapper": "ooo",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ooo:
    class Meta:
        name = "ooo"

    qqq: Optional[Qqq] = field(
        default=None,
        metadata={
            "wrapper": "ppp",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lll:
    class Meta:
        name = "lll"

    nnn: Optional[Nnn] = field(
        default=None,
        metadata={
            "wrapper": "mmm",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Mmm:
    class Meta:
        name = "mmm"

    ooo: Optional[Ooo] = field(
        default=None,
        metadata={
            "wrapper": "nnn",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Jjj:
    class Meta:
        name = "jjj"

    lll: Optional[Lll] = field(
        default=None,
        metadata={
            "wrapper": "kkk",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Kkk:
    class Meta:
        name = "kkk"

    mmm: Optional[Mmm] = field(
        default=None,
        metadata={
            "wrapper": "lll",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Hhh:
    class Meta:
        name = "hhh"

    jjj: Optional[Jjj] = field(
        default=None,
        metadata={
            "wrapper": "iii",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Iii:
    class Meta:
        name = "iii"

    kkk: Optional[Kkk] = field(
        default=None,
        metadata={
            "wrapper": "jjj",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Fff:
    class Meta:
        name = "fff"

    hhh: Optional[Hhh] = field(
        default=None,
        metadata={
            "wrapper": "ggg",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ggg:
    class Meta:
        name = "ggg"

    iii: Optional[Iii] = field(
        default=None,
        metadata={
            "wrapper": "hhh",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ddd:
    class Meta:
        name = "ddd"

    fff: Optional[Fff] = field(
        default=None,
        metadata={
            "wrapper": "eee",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Eee:
    class Meta:
        name = "eee"

    ggg: Optional[Ggg] = field(
        default=None,
        metadata={
            "wrapper": "fff",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Bbb:
    class Meta:
        name = "bbb"

    ddd: Optional[Ddd] = field(
        default=None,
        metadata={
            "wrapper": "ccc",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ccc:
    class Meta:
        name = "ccc"

    eee: Optional[Eee] = field(
        default=None,
        metadata={
            "wrapper": "ddd",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Aaa:
    class Meta:
        name = "aaa"

    ccc: Optional[Ccc] = field(
        default=None,
        metadata={
            "wrapper": "bbb",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    bbb: Optional[Bbb] = field(
        default=None,
        metadata={
            "wrapper": "aaa",
            "type": "Element",
            "required": True,
        },
    )
    w3_org_xml_1998_namespace_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
