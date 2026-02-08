from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Signatures:
    class Meta:
        name = "signatures"

    w3_org_2000_09_xmldsig_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass(kw_only=True)
class Yyy:
    class Meta:
        name = "yyy"

    signatures: Signatures = field(
        metadata={
            "wrapper": "zzz",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Zzz:
    class Meta:
        name = "zzz"

    signatures: Signatures = field(
        metadata={
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Www:
    class Meta:
        name = "www"

    yyy: Yyy = field(
        metadata={
            "wrapper": "xxx",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Xxx:
    class Meta:
        name = "xxx"

    zzz: Zzz = field(
        metadata={
            "wrapper": "yyy",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Ttt:
    class Meta:
        name = "ttt"

    www: Www = field(
        metadata={
            "wrapper": "uuu",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Uuu:
    class Meta:
        name = "uuu"

    xxx: Xxx = field(
        metadata={
            "wrapper": "www",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Rrr:
    class Meta:
        name = "rrr"

    ttt: Ttt = field(
        metadata={
            "wrapper": "sss",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Sss:
    class Meta:
        name = "sss"

    uuu: Uuu = field(
        metadata={
            "wrapper": "ttt",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Ppp:
    class Meta:
        name = "ppp"

    rrr: Rrr = field(
        metadata={
            "wrapper": "qqq",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Qqq:
    class Meta:
        name = "qqq"

    sss: Sss = field(
        metadata={
            "wrapper": "rrr",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Nnn:
    class Meta:
        name = "nnn"

    ppp: Ppp = field(
        metadata={
            "wrapper": "ooo",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Ooo:
    class Meta:
        name = "ooo"

    qqq: Qqq = field(
        metadata={
            "wrapper": "ppp",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Lll:
    class Meta:
        name = "lll"

    nnn: Nnn = field(
        metadata={
            "wrapper": "mmm",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Mmm:
    class Meta:
        name = "mmm"

    ooo: Ooo = field(
        metadata={
            "wrapper": "nnn",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Jjj:
    class Meta:
        name = "jjj"

    lll: Lll = field(
        metadata={
            "wrapper": "kkk",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Kkk:
    class Meta:
        name = "kkk"

    mmm: Mmm = field(
        metadata={
            "wrapper": "lll",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Hhh:
    class Meta:
        name = "hhh"

    jjj: Jjj = field(
        metadata={
            "wrapper": "iii",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Iii:
    class Meta:
        name = "iii"

    kkk: Kkk = field(
        metadata={
            "wrapper": "jjj",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Fff:
    class Meta:
        name = "fff"

    hhh: Hhh = field(
        metadata={
            "wrapper": "ggg",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Ggg:
    class Meta:
        name = "ggg"

    iii: Iii = field(
        metadata={
            "wrapper": "hhh",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Ddd:
    class Meta:
        name = "ddd"

    fff: Fff = field(
        metadata={
            "wrapper": "eee",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Eee:
    class Meta:
        name = "eee"

    ggg: Ggg = field(
        metadata={
            "wrapper": "fff",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Bbb:
    class Meta:
        name = "bbb"

    ddd: Ddd = field(
        metadata={
            "wrapper": "ccc",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Ccc:
    class Meta:
        name = "ccc"

    eee: Eee = field(
        metadata={
            "wrapper": "ddd",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Aaa:
    class Meta:
        name = "aaa"

    ccc: Ccc = field(
        metadata={
            "wrapper": "bbb",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    bbb: Bbb = field(
        metadata={
            "wrapper": "aaa",
            "type": "Element",
        }
    )
    w3_org_xml_1998_namespace_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
