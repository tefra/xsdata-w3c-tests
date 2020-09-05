from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-enumeration-4-NS"


class NistschemaSvIvListLanguageEnumeration4Type(Enum):
    """
    :cvar HA_HI_HR_HU_HY_IA_IE_IK:
    :cvar BG_BH_BI_BN_BO_BR_CA:
    :cvar SS_ST_SU_SV_SW:
    :cvar MR_MS_MT_MY_NA_NE_NL_NO_OC:
    :cvar RN_RO_RU_RW_SA_SD_SG_SH_SI:
    :cvar ES_ET_EU_FA_FI:
    :cvar IS_IT_IW_JA_JI:
    :cvar HR_HU_HY_IA_IE_IK:
    """
    HA_HI_HR_HU_HY_IA_IE_IK = "HA HI HR HU HY IA IE IK"
    BG_BH_BI_BN_BO_BR_CA = "BG BH BI BN BO BR CA"
    SS_ST_SU_SV_SW = "SS ST SU SV SW"
    MR_MS_MT_MY_NA_NE_NL_NO_OC = "MR MS MT MY NA NE NL NO OC"
    RN_RO_RU_RW_SA_SD_SG_SH_SI = "RN RO RU RW SA SD SG SH SI"
    ES_ET_EU_FA_FI = "ES ET EU FA FI"
    IS_IT_IW_JA_JI = "IS IT IW JA JI"
    HR_HU_HY_IA_IE_IK = "HR HU HY IA IE IK"


@dataclass
class NistschemaSvIvListLanguageEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-language-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-language-enumeration-4-NS"

    value: Optional[NistschemaSvIvListLanguageEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
