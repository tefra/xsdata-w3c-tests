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
class Yyy:
    class Meta:
        name = "yyy"

    zzz: Optional[Zzz] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Xxx:
    class Meta:
        name = "xxx"

    yyy: Optional[Yyy] = field(
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

    xxx: Optional[Xxx] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Uuu:
    class Meta:
        name = "uuu"

    www: Optional[Www] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ttt:
    class Meta:
        name = "ttt"

    uuu: Optional[Uuu] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Sss:
    class Meta:
        name = "sss"

    ttt: Optional[Ttt] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Rrr:
    class Meta:
        name = "rrr"

    sss: Optional[Sss] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Qqq:
    class Meta:
        name = "qqq"

    rrr: Optional[Rrr] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ppp:
    class Meta:
        name = "ppp"

    qqq: Optional[Qqq] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ooo:
    class Meta:
        name = "ooo"

    ppp: Optional[Ppp] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Nnn:
    class Meta:
        name = "nnn"

    ooo: Optional[Ooo] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Mmm:
    class Meta:
        name = "mmm"

    nnn: Optional[Nnn] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lll:
    class Meta:
        name = "lll"

    mmm: Optional[Mmm] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Kkk:
    class Meta:
        name = "kkk"

    lll: Optional[Lll] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Jjj:
    class Meta:
        name = "jjj"

    kkk: Optional[Kkk] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Iii:
    class Meta:
        name = "iii"

    jjj: Optional[Jjj] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Hhh:
    class Meta:
        name = "hhh"

    iii: Optional[Iii] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ggg:
    class Meta:
        name = "ggg"

    hhh: Optional[Hhh] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Fff:
    class Meta:
        name = "fff"

    ggg: Optional[Ggg] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Eee:
    class Meta:
        name = "eee"

    fff: Optional[Fff] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ddd:
    class Meta:
        name = "ddd"

    eee: Optional[Eee] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ccc:
    class Meta:
        name = "ccc"

    ddd: Optional[Ddd] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Bbb:
    class Meta:
        name = "bbb"

    ccc: Optional[Ccc] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Aaa:
    class Meta:
        name = "aaa"

    bbb: Optional[Bbb] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    aaa: Optional[Aaa] = field(
        default=None,
        metadata={
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
