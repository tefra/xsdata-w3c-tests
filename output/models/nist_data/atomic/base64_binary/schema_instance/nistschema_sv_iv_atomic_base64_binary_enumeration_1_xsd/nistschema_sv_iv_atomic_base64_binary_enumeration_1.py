from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-1-NS"


class NistschemaSvIvAtomicBase64BinaryEnumeration1Type(Enum):
    """
    :cvar ZM_FYAML5_ZM1I:
    :cvar D_HJH_ZWJMC3_ZHCG:
    :cvar Y29ZA_XB5AMTV_ZNHWB2LPANHV_ZN_RRC_HVXA3_BYBN_BY_ZGHJE_HR3C2DQC_GRRDM_FQBM9SE_XHYE_HZZ_YN_FJ_ZM10:
    :cvar B250_Z21MB2X5B_GLU_YMDUANDPBN_BWB3_V1_YWHQD2_NID_A:
    :cvar C3_RJB2XYCND2B_WPZA29WDMDJBNK:
    """
    ZM_FYAML5_ZM1I = "ZmFyaml5Zm1i"
    D_HJH_ZWJMC3_ZHCG = "dHJhZWJmc3Zhcg=="
    Y29ZA_XB5AMTV_ZNHWB2LPANHV_ZN_RRC_HVXA3_BYBN_BY_ZGHJE_HR3C2DQC_GRRDM_FQBM9SE_XHYE_HZZ_YN_FJ_ZM10 = "Y29zaXB5amtvZnhwb2lpanhvZnRrcHVxa3BybnByZGhjeHR3c2dqcGRrdmFqbm9seXhyeHZzYnFjZm10"
    B250_Z21MB2X5B_GLU_YMDUANDPBN_BWB3_V1_YWHQD2_NID_A = "b250Z21mb2x5bGluYmduandpbnBwb3V1YWhqd2NidA=="
    C3_RJB2XYCND2B_WPZA29WDMDJBNK = "c3Rjb2xycnd2bWpza29wdmdjbnk="


@dataclass
class NistschemaSvIvAtomicBase64BinaryEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicBase64BinaryEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
