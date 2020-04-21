from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar H:
    :cvar H111:
    :cvar HHHH:
    :cvar I_I:
    :cvar I11_I:
    :cvar III_I:
    :cvar J_J:
    :cvar J1_J1:
    :cvar JJ_JJ:
    :cvar K_KK:
    :cvar K1_KK:
    :cvar KK_KK:
    :cvar LL:
    :cvar LL11:
    :cvar LLLL:
    :cvar MM_M:
    :cvar MM1_M:
    :cvar MMM_M:
    :cvar NNN:
    :cvar NNN1:
    :cvar NNNN:
    :cvar OOOO:
    :cvar AAAA:
    :cvar BBB0:
    :cvar BBB_B:
    :cvar BBB:
    :cvar CC0C:
    :cvar CC_CC:
    :cvar CC_C:
    :cvar DD00:
    :cvar DD_DD:
    :cvar DD:
    :cvar E0EE:
    :cvar E_EEE:
    :cvar E_EE:
    :cvar F0F0:
    :cvar F_FF_F:
    :cvar F_F:
    :cvar G000:
    :cvar G_GGG:
    :cvar G:
    :cvar P00P:
    :cvar P_PPP:
    :cvar P_P:
    """
    H = "H---"
    H111 = "H111"
    HHHH = "Hhhh"
    I_I = "I--I"
    I11_I = "I11I"
    III_I = "IiiI"
    J_J = "J-J-"
    J1_J1 = "J1J1"
    JJ_JJ = "JjJj"
    K_KK = "K-KK"
    K1_KK = "K1KK"
    KK_KK = "KkKK"
    LL = "LL--"
    LL11 = "LL11"
    LLLL = "LLll"
    MM_M = "MM-M"
    MM1_M = "MM1M"
    MMM_M = "MMmM"
    NNN = "NNN-"
    NNN1 = "NNN1"
    NNNN = "NNNn"
    OOOO = "OOOO"
    AAAA = "aaaa"
    BBB0 = "bbb0"
    BBB_B = "bbbB"
    BBB = "bbb_"
    CC0C = "cc0c"
    CC_CC = "ccCc"
    CC_C = "cc_c"
    DD00 = "dd00"
    DD_DD = "ddDD"
    DD = "dd__"
    E0EE = "e0ee"
    E_EEE = "eEee"
    E_EE = "e_ee"
    F0F0 = "f0f0"
    F_FF_F = "fFfF"
    F_F = "f_f_"
    G000 = "g000"
    G_GGG = "gGGG"
    G = "g___"
    P00P = "p00p"
    P_PPP = "pPPp"
    P_P = "p__p"


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
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
