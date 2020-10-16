from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar AAAA:
    :cvar BBB_B:
    :cvar CC_CC:
    :cvar DD_DD:
    :cvar E_EEE:
    :cvar F_FF_F:
    :cvar P_PPP:
    :cvar G_GGG:
    :cvar HHHH:
    :cvar III_I:
    :cvar JJ_JJ:
    :cvar KK_KK:
    :cvar LLLL:
    :cvar MMM_M:
    :cvar NNNN:
    :cvar OOOO:
    :cvar BBB0:
    :cvar CC0C:
    :cvar DD00:
    :cvar E0EE:
    :cvar F0F0:
    :cvar P00P:
    :cvar G000:
    :cvar BBB:
    :cvar CC_C:
    :cvar DD:
    :cvar E_EE:
    :cvar F_F:
    :cvar P_P:
    :cvar G:
    :cvar H111:
    :cvar I11_I:
    :cvar J1_J1:
    :cvar K1_KK:
    :cvar LL11:
    :cvar MM1_M:
    :cvar NNN1:
    :cvar H:
    :cvar I_I:
    :cvar J_J:
    :cvar K_KK:
    :cvar LL:
    :cvar MM_M:
    :cvar NNN:
    """
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


@dataclass
class Root:
    """
    :ivar val:
    """
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    val: List[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
