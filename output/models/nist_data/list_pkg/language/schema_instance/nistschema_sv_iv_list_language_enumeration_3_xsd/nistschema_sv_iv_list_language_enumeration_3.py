from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-enumeration-3-NS"


class NistschemaSvIvListLanguageEnumeration3Type(Enum):
    SK_SL_SM_SN_SO_SQ_SR_SS_ST = "SK SL SM SN SO SQ SR SS ST"
    KK_KL_KM_KN_KO_KS = "KK KL KM KN KO KS"
    MN_MO_MR_MS_MT_MY = "MN MO MR MS MT MY"
    ET_EU_FA_FI_FJ = "ET EU FA FI FJ"
    OR_PA_PL_PS_PT_QU_RM_RN = "OR PA PL PS PT QU RM RN"
    SI_SK_SL_SM_SN_SO_SQ_SR_SS = "SI SK SL SM SN SO SQ SR SS"
    BI_BN_BO_BR_CA_CO = "BI BN BO BR CA CO"
    HA_HI_HR_HU_HY = "HA HI HR HU HY"
    MR_MS_MT_MY_NA = "MR MS MT MY NA"
    TW_UK_UR_UZ_VI_VO_WO_XH = "TW UK UR UZ VI VO WO XH"


@dataclass
class NistschemaSvIvListLanguageEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-language-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-language-enumeration-3-NS"

    value: Optional[NistschemaSvIvListLanguageEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
