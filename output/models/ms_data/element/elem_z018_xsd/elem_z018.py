from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Signatures:
    """
    :ivar w3_org_2000_09_xmldsig_element:
    """
    class Meta:
        name = "signatures"

    w3_org_2000_09_xmldsig_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://www.w3.org/2000/09/xmldsig#",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Zzz:
    """
    :ivar signatures:
    """
    class Meta:
        name = "zzz"

    signatures: Optional[Signatures] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Yyy:
    """
    :ivar zzz:
    """
    class Meta:
        name = "yyy"

    zzz: Optional[Zzz] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Xxx:
    """
    :ivar yyy:
    """
    class Meta:
        name = "xxx"

    yyy: Optional[Yyy] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Www:
    """
    :ivar xxx:
    """
    class Meta:
        name = "www"

    xxx: Optional[Xxx] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Uuu:
    """
    :ivar www:
    """
    class Meta:
        name = "uuu"

    www: Optional[Www] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Ttt:
    """
    :ivar uuu:
    """
    class Meta:
        name = "ttt"

    uuu: Optional[Uuu] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Sss:
    """
    :ivar ttt:
    """
    class Meta:
        name = "sss"

    ttt: Optional[Ttt] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Rrr:
    """
    :ivar sss:
    """
    class Meta:
        name = "rrr"

    sss: Optional[Sss] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Qqq:
    """
    :ivar rrr:
    """
    class Meta:
        name = "qqq"

    rrr: Optional[Rrr] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Ppp:
    """
    :ivar qqq:
    """
    class Meta:
        name = "ppp"

    qqq: Optional[Qqq] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Ooo:
    """
    :ivar ppp:
    """
    class Meta:
        name = "ooo"

    ppp: Optional[Ppp] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Nnn:
    """
    :ivar ooo:
    """
    class Meta:
        name = "nnn"

    ooo: Optional[Ooo] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Mmm:
    """
    :ivar nnn:
    """
    class Meta:
        name = "mmm"

    nnn: Optional[Nnn] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Lll:
    """
    :ivar mmm:
    """
    class Meta:
        name = "lll"

    mmm: Optional[Mmm] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Kkk:
    """
    :ivar lll:
    """
    class Meta:
        name = "kkk"

    lll: Optional[Lll] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Jjj:
    """
    :ivar kkk:
    """
    class Meta:
        name = "jjj"

    kkk: Optional[Kkk] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Iii:
    """
    :ivar jjj:
    """
    class Meta:
        name = "iii"

    jjj: Optional[Jjj] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Hhh:
    """
    :ivar iii:
    """
    class Meta:
        name = "hhh"

    iii: Optional[Iii] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Ggg:
    """
    :ivar hhh:
    """
    class Meta:
        name = "ggg"

    hhh: Optional[Hhh] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Fff:
    """
    :ivar ggg:
    """
    class Meta:
        name = "fff"

    ggg: Optional[Ggg] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Eee:
    """
    :ivar fff:
    """
    class Meta:
        name = "eee"

    fff: Optional[Fff] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Ddd:
    """
    :ivar eee:
    """
    class Meta:
        name = "ddd"

    eee: Optional[Eee] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Ccc:
    """
    :ivar ddd:
    """
    class Meta:
        name = "ccc"

    ddd: Optional[Ddd] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Bbb:
    """
    :ivar ccc:
    """
    class Meta:
        name = "bbb"

    ccc: Optional[Ccc] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Aaa:
    """
    :ivar bbb:
    """
    class Meta:
        name = "aaa"

    bbb: Optional[Bbb] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar aaa:
    :ivar w3_org_xml_1998_namespace_attributes:
    """
    class Meta:
        name = "root"

    aaa: Optional[Aaa] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    w3_org_xml_1998_namespace_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
