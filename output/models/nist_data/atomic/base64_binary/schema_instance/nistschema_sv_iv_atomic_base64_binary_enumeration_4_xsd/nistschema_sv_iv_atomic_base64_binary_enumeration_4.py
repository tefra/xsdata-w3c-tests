from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-4-NS"


class NistschemaSvIvAtomicBase64BinaryEnumeration4Type(Enum):
    A_GO = b"hj"
    YWZKC_WD2A2_ZZC_HN5CN_NJB_WF3E_GR2_Z3_NWA2XKD_WD4_YXBLC_HLUD_GFVCMD3E_WJSB_HLZ = b"afdqgvkfspsyrscmawxdvgspkldugxapepyntaorgwybllys"
    D_W15ANLKE_WXU_ZHHKA_XF1_ZWL0B_HNMA2PLE_XRHD3_VI_YMLXE_G9RE_XNL_ZXV5C2_NI_Y3L5A_WTLC21XD_HNPA_WDVB_A = b"umyjydylndxdiqueitlsfkjeytawubbiqxokyseeuyscbcyyikesmqtsiigol"
    C3_RMD_HZOE_GFMD_HF3A_WJM_YW9WDMLI_Y3_JI_ZA = b"stftvhxaftqwibfaopvibcrbd"
    ZXJUE_G91C_G9Z_YMTWC_XZLE_GHME_HLJC3_RSD_WDQC_XA = b"ernxouposbkpqvexhfxycstlugjqp"
    D_HJNA3_FSC_XJ1A_HVW_Z2H5D_GX5B_XV1D2XPD_GXX_YN_BQA_WJWC_HDM_ZGXH_Z25TDN_N2_ZHFTD_GJHA_XLICN_ZQD_GVIA_WTH_YWV3 = b"trgkqlqruhupghytlymuuwlitlqbpjibppwfdlagnmvsvdqmtbaiybrvjtebikaaew"
    YM_Z1C21MD3_R2BMD3BN_Z4CN_RUB_G15C_HJHAM_FSB2_RSCG = b"bfusmfwtvngwnvxrtnlmyprajalodlr"


@dataclass
class NistschemaSvIvAtomicBase64BinaryEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicBase64BinaryEnumeration4Type] = field(
        default=None,
        metadata={
            "format": "base64",
        }
    )
