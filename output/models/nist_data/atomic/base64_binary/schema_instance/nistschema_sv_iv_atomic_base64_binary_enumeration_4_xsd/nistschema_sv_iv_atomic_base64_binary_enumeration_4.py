from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-4-NS"


class NistschemaSvIvAtomicBase64BinaryEnumeration4Type(Enum):
    """
    :cvar A_GO:
    :cvar YWZKC_WD2A2_ZZC_HN5CN_NJB_WF3E_GR2_Z3_NWA2XKD_WD4_YXBLC_HLUD_GFVCMD3E_WJSB_HLZ:
    :cvar D_W15ANLKE_WXU_ZHHKA_XF1_ZWL0B_HNMA2PLE_XRHD3_VI_YMLXE_G9RE_XNL_ZXV5C2_NI_Y3L5A_WTLC21XD_HNPA_WDVB_A:
    :cvar C3_RMD_HZOE_GFMD_HF3A_WJM_YW9WDMLI_Y3_JI_ZA:
    :cvar ZXJUE_G91C_G9Z_YMTWC_XZLE_GHME_HLJC3_RSD_WDQC_XA:
    :cvar D_HJNA3_FSC_XJ1A_HVW_Z2H5D_GX5B_XV1D2XPD_GXX_YN_BQA_WJWC_HDM_ZGXH_Z25TDN_N2_ZHFTD_GJHA_XLICN_ZQD_GVIA_WTH_YWV3:
    :cvar YM_Z1C21MD3_R2BMD3BN_Z4CN_RUB_G15C_HJHAM_FSB2_RSCG:
    """
    A_GO = "aGo="
    YWZKC_WD2A2_ZZC_HN5CN_NJB_WF3E_GR2_Z3_NWA2XKD_WD4_YXBLC_HLUD_GFVCMD3E_WJSB_HLZ = "YWZkcWd2a2ZzcHN5cnNjbWF3eGR2Z3Nwa2xkdWd4YXBlcHludGFvcmd3eWJsbHlz"
    D_W15ANLKE_WXU_ZHHKA_XF1_ZWL0B_HNMA2PLE_XRHD3_VI_YMLXE_G9RE_XNL_ZXV5C2_NI_Y3L5A_WTLC21XD_HNPA_WDVB_A = "dW15anlkeWxuZHhkaXF1ZWl0bHNma2pleXRhd3ViYmlxeG9reXNlZXV5c2NiY3l5aWtlc21xdHNpaWdvbA=="
    C3_RMD_HZOE_GFMD_HF3A_WJM_YW9WDMLI_Y3_JI_ZA = "c3RmdHZoeGFmdHF3aWJmYW9wdmliY3JiZA=="
    ZXJUE_G91C_G9Z_YMTWC_XZLE_GHME_HLJC3_RSD_WDQC_XA = "ZXJueG91cG9zYmtwcXZleGhmeHljc3RsdWdqcXA="
    D_HJNA3_FSC_XJ1A_HVW_Z2H5D_GX5B_XV1D2XPD_GXX_YN_BQA_WJWC_HDM_ZGXH_Z25TDN_N2_ZHFTD_GJHA_XLICN_ZQD_GVIA_WTH_YWV3 = "dHJna3FscXJ1aHVwZ2h5dGx5bXV1d2xpdGxxYnBqaWJwcHdmZGxhZ25tdnN2ZHFtdGJhaXlicnZqdGViaWthYWV3"
    YM_Z1C21MD3_R2BMD3BN_Z4CN_RUB_G15C_HJHAM_FSB2_RSCG = "YmZ1c21md3R2bmd3bnZ4cnRubG15cHJhamFsb2Rscg=="


@dataclass
class NistschemaSvIvAtomicBase64BinaryEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicBase64BinaryEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
