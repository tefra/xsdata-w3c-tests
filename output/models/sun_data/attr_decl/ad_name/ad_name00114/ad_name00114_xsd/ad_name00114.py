from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    aaaa: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bbb_b: Optional[int] = field(
        default=None,
        metadata={
            "name": "bbbB",
            "type": "Attribute",
        }
    )
    cc_cc: Optional[int] = field(
        default=None,
        metadata={
            "name": "ccCc",
            "type": "Attribute",
        }
    )
    dd_dd: Optional[int] = field(
        default=None,
        metadata={
            "name": "ddDD",
            "type": "Attribute",
        }
    )
    e_eee: Optional[int] = field(
        default=None,
        metadata={
            "name": "eEee",
            "type": "Attribute",
        }
    )
    f_ff_f: Optional[int] = field(
        default=None,
        metadata={
            "name": "fFfF",
            "type": "Attribute",
        }
    )
    p_ppp: Optional[int] = field(
        default=None,
        metadata={
            "name": "pPPp",
            "type": "Attribute",
        }
    )
    g_ggg: Optional[int] = field(
        default=None,
        metadata={
            "name": "gGGG",
            "type": "Attribute",
        }
    )
    hhhh: Optional[int] = field(
        default=None,
        metadata={
            "name": "Hhhh",
            "type": "Attribute",
        }
    )
    iii_i: Optional[int] = field(
        default=None,
        metadata={
            "name": "IiiI",
            "type": "Attribute",
        }
    )
    jj_jj: Optional[int] = field(
        default=None,
        metadata={
            "name": "JjJj",
            "type": "Attribute",
        }
    )
    kk_kk: Optional[int] = field(
        default=None,
        metadata={
            "name": "KkKK",
            "type": "Attribute",
        }
    )
    llll: Optional[int] = field(
        default=None,
        metadata={
            "name": "LLll",
            "type": "Attribute",
        }
    )
    mmm_m: Optional[int] = field(
        default=None,
        metadata={
            "name": "MMmM",
            "type": "Attribute",
        }
    )
    nnnn: Optional[int] = field(
        default=None,
        metadata={
            "name": "NNNn",
            "type": "Attribute",
        }
    )
    oooo: Optional[int] = field(
        default=None,
        metadata={
            "name": "OOOO",
            "type": "Attribute",
        }
    )
    bbb0: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cc0c: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dd00: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    e0ee: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    f0f0: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    p00p: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    g000: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bbb: Optional[int] = field(
        default=None,
        metadata={
            "name": "bbb_",
            "type": "Attribute",
        }
    )
    cc_c: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dd: Optional[int] = field(
        default=None,
        metadata={
            "name": "dd__",
            "type": "Attribute",
        }
    )
    e_ee: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    f_f: Optional[int] = field(
        default=None,
        metadata={
            "name": "f_f_",
            "type": "Attribute",
        }
    )
    p_p: Optional[int] = field(
        default=None,
        metadata={
            "name": "p__p",
            "type": "Attribute",
        }
    )
    g: Optional[int] = field(
        default=None,
        metadata={
            "name": "g___",
            "type": "Attribute",
        }
    )
    h111: Optional[int] = field(
        default=None,
        metadata={
            "name": "H111",
            "type": "Attribute",
        }
    )
    i11_i: Optional[int] = field(
        default=None,
        metadata={
            "name": "I11I",
            "type": "Attribute",
        }
    )
    j1_j1: Optional[int] = field(
        default=None,
        metadata={
            "name": "J1J1",
            "type": "Attribute",
        }
    )
    k1_kk: Optional[int] = field(
        default=None,
        metadata={
            "name": "K1KK",
            "type": "Attribute",
        }
    )
    ll11: Optional[int] = field(
        default=None,
        metadata={
            "name": "LL11",
            "type": "Attribute",
        }
    )
    mm1_m: Optional[int] = field(
        default=None,
        metadata={
            "name": "MM1M",
            "type": "Attribute",
        }
    )
    nnn1: Optional[int] = field(
        default=None,
        metadata={
            "name": "NNN1",
            "type": "Attribute",
        }
    )
    h: Optional[int] = field(
        default=None,
        metadata={
            "name": "H---",
            "type": "Attribute",
        }
    )
    i_i: Optional[int] = field(
        default=None,
        metadata={
            "name": "I--I",
            "type": "Attribute",
        }
    )
    j_j: Optional[int] = field(
        default=None,
        metadata={
            "name": "J-J-",
            "type": "Attribute",
        }
    )
    k_kk: Optional[int] = field(
        default=None,
        metadata={
            "name": "K-KK",
            "type": "Attribute",
        }
    )
    ll: Optional[int] = field(
        default=None,
        metadata={
            "name": "LL--",
            "type": "Attribute",
        }
    )
    mm_m: Optional[int] = field(
        default=None,
        metadata={
            "name": "MM-M",
            "type": "Attribute",
        }
    )
    nnn: Optional[int] = field(
        default=None,
        metadata={
            "name": "NNN-",
            "type": "Attribute",
        }
    )
