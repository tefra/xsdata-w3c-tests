from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar AAAA:
    :cvar BBB:
    :cvar BBB0:
    :cvar BBB_B:
    :cvar CC0C:
    :cvar CC_C:
    :cvar CC_CC:
    :cvar DD:
    :cvar DD00:
    :cvar DD_DD:
    :cvar E0EE:
    :cvar E_EE:
    :cvar E_EEE:
    :cvar F0F0:
    :cvar F_F:
    :cvar F_FF_F:
    :cvar G:
    :cvar G000:
    :cvar G_GGG:
    :cvar H:
    :cvar H111:
    :cvar HHHH:
    :cvar I11_I:
    :cvar III_I:
    :cvar I_I:
    :cvar J1_J1:
    :cvar JJ_JJ:
    :cvar J_J:
    :cvar K1_KK:
    :cvar KK_KK:
    :cvar K_KK:
    :cvar LL:
    :cvar LL11:
    :cvar LLLL:
    :cvar MM1_M:
    :cvar MMM_M:
    :cvar MM_M:
    :cvar NNN:
    :cvar NNN1:
    :cvar NNNN:
    :cvar OOOO:
    :cvar P00P:
    :cvar P_P:
    :cvar P_PPP:
    """
    AAAA = "aaaa"
    BBB = "bbb_"
    BBB0 = "bbb0"
    BBB_B = "bbbB"
    CC0C = "cc0c"
    CC_C = "cc_c"
    CC_CC = "ccCc"
    DD = "dd__"
    DD00 = "dd00"
    DD_DD = "ddDD"
    E0EE = "e0ee"
    E_EE = "e_ee"
    E_EEE = "eEee"
    F0F0 = "f0f0"
    F_F = "f_f_"
    F_FF_F = "fFfF"
    G = "g___"
    G000 = "g000"
    G_GGG = "gGGG"
    H = "H---"
    H111 = "H111"
    HHHH = "Hhhh"
    I11_I = "I11I"
    III_I = "IiiI"
    I_I = "I--I"
    J1_J1 = "J1J1"
    JJ_JJ = "JjJj"
    J_J = "J-J-"
    K1_KK = "K1KK"
    KK_KK = "KkKK"
    K_KK = "K-KK"
    LL = "LL--"
    LL11 = "LL11"
    LLLL = "LLll"
    MM1_M = "MM1M"
    MMM_M = "MMmM"
    MM_M = "MM-M"
    NNN = "NNN-"
    NNN1 = "NNN1"
    NNNN = "NNNn"
    OOOO = "OOOO"
    P00P = "p00p"
    P_P = "p__p"
    P_PPP = "pPPp"


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
