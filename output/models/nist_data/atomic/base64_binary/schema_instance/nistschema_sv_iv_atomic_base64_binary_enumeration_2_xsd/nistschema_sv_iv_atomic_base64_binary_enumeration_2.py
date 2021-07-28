from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-2-NS"


class NistschemaSvIvAtomicBase64BinaryEnumeration2Type(Enum):
    DMXPB_XRPBN_J3A_WLWAMP3_ZXHI_ZXJ0C_XBX = b"vlimtinrwiipjjwexbertqpq"
    D2XNBM_NK_ZWN4_ZWZLE_HNQ_YXZKC2XLC_XRIDN_Z1A_XV0A_GHZDM_Z0_ZWXWBNDI_ZMLN = b"wlgncdecxefexsjavdsleqtbvvuiuthhsvftelpnwbfig"
    ZGDQB_G5HC2TZE_WN2B_W5QC_HDHCNHUCN_FND_XZIC_XF5CM_RJ = b"dgjlnasksycvmnjpwarxnrqguvbqqyrdc"
    ZHFZB_WXNB_WVW = b"dqsmlgmep"
    D_GVMD3_BSB_WRM_Y3HTC_G1KD2_JOA_WZTCNHOB_XZL_YWVN_YXRL_YWXWBM1ME_W14D_XU = b"tefwplmdfcxmpmdwbhifmrxhmveaegatealpnmfymxuu"
    C_WFO_YND1D_GZLE_WV3D3_RRA3_NPBN_FI_ZGNQAMDRC_WF4_YXZ5_Y3_RI = b"qahbwutfeyewwtkksinqbdcjjgkqaxavyctb"
    C2DMC2_ZH_ZXBU_ZGZN_Y214_Z2_RSD2_N4AM1HB_XL3_ZGRU_Y3HPC_HZSC_HLZE_WPK_ZHNWC_GDWB_GLP_ZXJZA_HRQAW = b"sgfsfaepndfgcmxgdlwcxjmamywddncxipvlpysyjddsppgpliiershtjk"
    D_XZI_Z3_RKC_GXW_Z3HKC3_FQE_GZTCM_VSB_HNQA_W5QE_HLMA2_Z5B_XZI_YM_VR_ZM_Z2_Z2XXD_HB4B_W5YC_HZ0AN_Z2AMTVD2_N1A_WH2D_WDI_ZGLTDW = b"uvbgtdplpgxdsqjxfmrellsjinjxyfkfymvbbekffvglqtpxmnrpvtjvvjkowcuihvugbdimw"
    D3_N5C_HJO_Z250A_WTM_YML2_ZGN2B_GZ4CN_ZK = b"wsyprhgntikfbivdcvlfxrvd"


@dataclass
class NistschemaSvIvAtomicBase64BinaryEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicBase64BinaryEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
