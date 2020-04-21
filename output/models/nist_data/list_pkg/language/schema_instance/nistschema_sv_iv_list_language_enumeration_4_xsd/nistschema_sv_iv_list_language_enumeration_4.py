from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-enumeration-4-NS"


class NistschemaSvIvListLanguageEnumeration4Type(Enum):
    """
    :cvar BG_BH_BI_BN_BO_BR_CA:
    :cvar ES_ET_EU_FA_FI:
    :cvar HA_HI_HR_HU_HY_IA_IE_IK:
    :cvar HR_HU_HY_IA_IE_IK:
    :cvar IS_IT_IW_JA_JI:
    :cvar MR_MS_MT_MY_NA_NE_NL_NO_OC:
    :cvar RN_RO_RU_RW_SA_SD_SG_SH_SI:
    :cvar SS_ST_SU_SV_SW:
    """
    BG_BH_BI_BN_BO_BR_CA = "BG BH BI BN BO BR CA"
    ES_ET_EU_FA_FI = "ES ET EU FA FI"
    HA_HI_HR_HU_HY_IA_IE_IK = "HA HI HR HU HY IA IE IK"
    HR_HU_HY_IA_IE_IK = "HR HU HY IA IE IK"
    IS_IT_IW_JA_JI = "IS IT IW JA JI"
    MR_MS_MT_MY_NA_NE_NL_NO_OC = "MR MS MT MY NA NE NL NO OC"
    RN_RO_RU_RW_SA_SD_SG_SH_SI = "RN RO RU RW SA SD SG SH SI"
    SS_ST_SU_SV_SW = "SS ST SU SV SW"


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
