from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-enumeration-5-NS"


class NistschemaSvIvListLanguageEnumeration5Type(Enum):
    """
    :cvar SL_SM_SN_SO_SQ_SR_SS_ST:
    :cvar IN_IS_IT_IW_JA:
    :cvar OM_OR_PA_PL_PS_PT_QU_RM_RN:
    :cvar SR_SS_ST_SU_SV_SW:
    :cvar BA_BE_BG_BH_BI_BN_BO_BR_CA:
    :cvar BE_BG_BH_BI_BN_BO_BR_CA_CO:
    :cvar HU_HY_IA_IE_IK_IN:
    :cvar SM_SN_SO_SQ_SR_SS_ST:
    :cvar IS_IT_IW_JA_JI_JW_KA_KK_KL:
    """
    SL_SM_SN_SO_SQ_SR_SS_ST = "SL SM SN SO SQ SR SS ST"
    IN_IS_IT_IW_JA = "IN IS IT IW JA"
    OM_OR_PA_PL_PS_PT_QU_RM_RN = "OM OR PA PL PS PT QU RM RN"
    SR_SS_ST_SU_SV_SW = "SR SS ST SU SV SW"
    BA_BE_BG_BH_BI_BN_BO_BR_CA = "BA BE BG BH BI BN BO BR CA"
    BE_BG_BH_BI_BN_BO_BR_CA_CO = "BE BG BH BI BN BO BR CA CO"
    HU_HY_IA_IE_IK_IN = "HU HY IA IE IK IN"
    SM_SN_SO_SQ_SR_SS_ST = "SM SN SO SQ SR SS ST"
    IS_IT_IW_JA_JI_JW_KA_KK_KL = "IS IT IW JA JI JW KA KK KL"


@dataclass
class NistschemaSvIvListLanguageEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-language-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-language-enumeration-5-NS"

    value: Optional[NistschemaSvIvListLanguageEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
