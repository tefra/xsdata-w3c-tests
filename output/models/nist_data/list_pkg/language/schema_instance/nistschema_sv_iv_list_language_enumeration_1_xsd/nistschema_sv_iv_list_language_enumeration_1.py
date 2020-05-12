from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-enumeration-1-NS"


class NistschemaSvIvListLanguageEnumeration1Type(Enum):
    """
    :cvar TL_TN_TO_TR_TS_TT_TW:
    :cvar MS_MT_MY_NA_NE_NL_NO_OC:
    :cvar EO_ES_ET_EU_FA_FI_FJ:
    :cvar PT_QU_RM_RN_RO_RU_RW_SA_SD:
    :cvar NA_NE_NL_NO_OC_OM_OR_PA_PL:
    :cvar KN_KO_KS_KU_KY_LA:
    :cvar SS_ST_SU_SV_SW_TA_TE_TG_TH:
    :cvar SI_SK_SL_SM_SN_SO_SQ:
    :cvar SW_TA_TE_TG_TH_TI_TK_TL_TN:
    """
    TL_TN_TO_TR_TS_TT_TW = "TL TN TO TR TS TT TW"
    MS_MT_MY_NA_NE_NL_NO_OC = "MS MT MY NA NE NL NO OC"
    EO_ES_ET_EU_FA_FI_FJ = "EO ES ET EU FA FI FJ"
    PT_QU_RM_RN_RO_RU_RW_SA_SD = "PT QU RM RN RO RU RW SA SD"
    NA_NE_NL_NO_OC_OM_OR_PA_PL = "NA NE NL NO OC OM OR PA PL"
    KN_KO_KS_KU_KY_LA = "KN KO KS KU KY LA"
    SS_ST_SU_SV_SW_TA_TE_TG_TH = "SS ST SU SV SW TA TE TG TH"
    SI_SK_SL_SM_SN_SO_SQ = "SI SK SL SM SN SO SQ"
    SW_TA_TE_TG_TH_TI_TK_TL_TN = "SW TA TE TG TH TI TK TL TN"


@dataclass
class NistschemaSvIvListLanguageEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-language-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-language-enumeration-1-NS"

    value: Optional[NistschemaSvIvListLanguageEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
