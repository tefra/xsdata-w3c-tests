from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-enumeration-2-NS"


class NistschemaSvIvListLanguageEnumeration2Type(Enum):
    """
    :cvar AM_AR_AS_AY_AZ_BA:
    :cvar CY_DA_DE_DZ_EL:
    :cvar FI_FJ_FO_FR_FY_GA_GD_GL_GN:
    :cvar IA_IE_IK_IN_IS_IT_IW_JA_JI:
    :cvar LN_LO_LT_LV_MG:
    :cvar SG_SH_SI_SK_SL_SM_SN:
    :cvar SS_ST_SU_SV_SW_TA_TE_TG:
    :cvar TH_TI_TK_TL_TN_TO_TR_TS_TT:
    """
    AM_AR_AS_AY_AZ_BA = "AM AR AS AY AZ BA"
    CY_DA_DE_DZ_EL = "CY DA DE DZ EL"
    FI_FJ_FO_FR_FY_GA_GD_GL_GN = "FI FJ FO FR FY GA GD GL GN"
    IA_IE_IK_IN_IS_IT_IW_JA_JI = "IA IE IK IN IS IT IW JA JI"
    LN_LO_LT_LV_MG = "LN LO LT LV MG"
    SG_SH_SI_SK_SL_SM_SN = "SG SH SI SK SL SM SN"
    SS_ST_SU_SV_SW_TA_TE_TG = "SS ST SU SV SW TA TE TG"
    TH_TI_TK_TL_TN_TO_TR_TS_TT = "TH TI TK TL TN TO TR TS TT"


@dataclass
class NistschemaSvIvListLanguageEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-language-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-language-enumeration-2-NS"

    value: Optional[NistschemaSvIvListLanguageEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )