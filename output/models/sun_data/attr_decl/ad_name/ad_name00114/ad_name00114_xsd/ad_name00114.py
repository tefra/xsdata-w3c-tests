from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    aaaa: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bbb_b: None | int = field(
        default=None,
        metadata={
            "name": "bbbB",
            "type": "Attribute",
        },
    )
    cc_cc: None | int = field(
        default=None,
        metadata={
            "name": "ccCc",
            "type": "Attribute",
        },
    )
    dd_dd: None | int = field(
        default=None,
        metadata={
            "name": "ddDD",
            "type": "Attribute",
        },
    )
    e_eee: None | int = field(
        default=None,
        metadata={
            "name": "eEee",
            "type": "Attribute",
        },
    )
    f_ff_f: None | int = field(
        default=None,
        metadata={
            "name": "fFfF",
            "type": "Attribute",
        },
    )
    p_ppp: None | int = field(
        default=None,
        metadata={
            "name": "pPPp",
            "type": "Attribute",
        },
    )
    g_ggg: None | int = field(
        default=None,
        metadata={
            "name": "gGGG",
            "type": "Attribute",
        },
    )
    hhhh: None | int = field(
        default=None,
        metadata={
            "name": "Hhhh",
            "type": "Attribute",
        },
    )
    iii_i: None | int = field(
        default=None,
        metadata={
            "name": "IiiI",
            "type": "Attribute",
        },
    )
    jj_jj: None | int = field(
        default=None,
        metadata={
            "name": "JjJj",
            "type": "Attribute",
        },
    )
    kk_kk: None | int = field(
        default=None,
        metadata={
            "name": "KkKK",
            "type": "Attribute",
        },
    )
    llll: None | int = field(
        default=None,
        metadata={
            "name": "LLll",
            "type": "Attribute",
        },
    )
    mmm_m: None | int = field(
        default=None,
        metadata={
            "name": "MMmM",
            "type": "Attribute",
        },
    )
    nnnn: None | int = field(
        default=None,
        metadata={
            "name": "NNNn",
            "type": "Attribute",
        },
    )
    oooo: None | int = field(
        default=None,
        metadata={
            "name": "OOOO",
            "type": "Attribute",
        },
    )
    bbb0: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cc0c: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dd00: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    e0ee: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    f0f0: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    p00p: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    g000: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bbb: None | int = field(
        default=None,
        metadata={
            "name": "bbb_",
            "type": "Attribute",
        },
    )
    cc_c: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dd: None | int = field(
        default=None,
        metadata={
            "name": "dd__",
            "type": "Attribute",
        },
    )
    e_ee: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    f_f: None | int = field(
        default=None,
        metadata={
            "name": "f_f_",
            "type": "Attribute",
        },
    )
    p_p: None | int = field(
        default=None,
        metadata={
            "name": "p__p",
            "type": "Attribute",
        },
    )
    g: None | int = field(
        default=None,
        metadata={
            "name": "g___",
            "type": "Attribute",
        },
    )
    h111: None | int = field(
        default=None,
        metadata={
            "name": "H111",
            "type": "Attribute",
        },
    )
    i11_i: None | int = field(
        default=None,
        metadata={
            "name": "I11I",
            "type": "Attribute",
        },
    )
    j1_j1: None | int = field(
        default=None,
        metadata={
            "name": "J1J1",
            "type": "Attribute",
        },
    )
    k1_kk: None | int = field(
        default=None,
        metadata={
            "name": "K1KK",
            "type": "Attribute",
        },
    )
    ll11: None | int = field(
        default=None,
        metadata={
            "name": "LL11",
            "type": "Attribute",
        },
    )
    mm1_m: None | int = field(
        default=None,
        metadata={
            "name": "MM1M",
            "type": "Attribute",
        },
    )
    nnn1: None | int = field(
        default=None,
        metadata={
            "name": "NNN1",
            "type": "Attribute",
        },
    )
    h: None | int = field(
        default=None,
        metadata={
            "name": "H---",
            "type": "Attribute",
        },
    )
    i_i: None | int = field(
        default=None,
        metadata={
            "name": "I--I",
            "type": "Attribute",
        },
    )
    j_j: None | int = field(
        default=None,
        metadata={
            "name": "J-J-",
            "type": "Attribute",
        },
    )
    k_kk: None | int = field(
        default=None,
        metadata={
            "name": "K-KK",
            "type": "Attribute",
        },
    )
    ll: None | int = field(
        default=None,
        metadata={
            "name": "LL--",
            "type": "Attribute",
        },
    )
    mm_m: None | int = field(
        default=None,
        metadata={
            "name": "MM-M",
            "type": "Attribute",
        },
    )
    nnn: None | int = field(
        default=None,
        metadata={
            "name": "NNN-",
            "type": "Attribute",
        },
    )
