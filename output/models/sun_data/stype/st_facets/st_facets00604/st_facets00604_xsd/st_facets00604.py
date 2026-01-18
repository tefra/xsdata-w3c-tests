from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    AAAA = "aaaa"
    BBB_B = "bbbB"
    CC_CC = "ccCc"
    DD_DD = "ddDD"
    E_EEE = "eEee"
    F_FF_F = "fFfF"
    P_PPP = "pPPp"
    G_GGG = "gGGG"
    HHHH = "Hhhh"
    III_I = "IiiI"
    JJ_JJ = "JjJj"
    KK_KK = "KkKK"
    LLLL = "LLll"
    MMM_M = "MMmM"
    NNNN = "NNNn"
    OOOO = "OOOO"
    BBB0 = "bbb0"
    CC0C = "cc0c"
    DD00 = "dd00"
    E0EE = "e0ee"
    F0F0 = "f0f0"
    P00P = "p00p"
    G000 = "g000"
    BBB = "bbb_"
    CC_C = "cc_c"
    DD = "dd__"
    E_EE = "e_ee"
    F_F = "f_f_"
    P_P = "p__p"
    G = "g___"
    H111 = "H111"
    I11_I = "I11I"
    J1_J1 = "J1J1"
    K1_KK = "K1KK"
    LL11 = "LL11"
    MM1_M = "MM1M"
    NNN1 = "NNN1"
    H = "H---"
    I_I = "I--I"
    J_J = "J-J-"
    K_KK = "K-KK"
    LL = "LL--"
    MM_M = "MM-M"
    NNN = "NNN-"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    val: list[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
