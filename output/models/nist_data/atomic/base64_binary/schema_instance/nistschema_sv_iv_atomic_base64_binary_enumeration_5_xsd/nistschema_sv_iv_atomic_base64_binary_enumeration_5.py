from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-5-NS"


class NistschemaSvIvAtomicBase64BinaryEnumeration5Type(Enum):
    """
    :cvar ZWNKBM_VKCN_JH_ZG9M_YMPWB3_JWC25IC3C:
    :cvar ZM_JK_Z3_FT_Y2H0D_XD5E_GRNB2_VZ_ZM_FOC25S_YWZTE_HZ4C_WNNC_WRZA_WXW_ZWNK_YMPTB_XRI_ZNC:
    :cvar AN_V0_YN_BV_Y2_JUE_XB0_YXBTC_HFYCN_FYB_WXVAN_FKE_XDT_Y3LLB3_N0BMDTBM_RX_YQ:
    :cvar C_GJ1B_GHKE_GZWC2HOA3_B3A_WTM_YWPQA_W5NB_GXKA_GLWANH0A_HLIA_W9QA_WNPDM_JPDM54C_Q:
    :cvar D_GDM_Y2DLBM_ZUDM14B_HF5_ZNLIE_XBRE_G9K_ZXV4CMXHAN_VJD_GDVB_XFQE_GLID_XNRE_W1UC_GJIA_GTKBN_B5_YWPSCW:
    :cvar D_WTYAM_FVD_GTJB_W93B_XBP_ZWHXC_GFXB_HB1A2_ZR_ZW95E_HN1B2PVA_XVYAM_VRE_G9Z_Y2P2BMDYB_W10A_HV5A2LSC_W1T_Y2THBW:
    :cvar E_HRHDN_FKA_XNX_ZQ:
    """
    ZWNKBM_VKCN_JH_ZG9M_YMPWB3_JWC25IC3C = "ZWNkbmVkcnJhZG9mYmpwb3Jwc25ic3c="
    ZM_JK_Z3_FT_Y2H0D_XD5E_GRNB2_VZ_ZM_FOC25S_YWZTE_HZ4C_WNNC_WRZA_WXW_ZWNK_YMPTB_XRI_ZNC = "ZmJkZ3FtY2h0dXd5eGRnb2VzZmFoc25sYWZteHZ4cWNncWRzaWxwZWNkYmptbXRiZnc="
    AN_V0_YN_BV_Y2_JUE_XB0_YXBTC_HFYCN_FYB_WXVAN_FKE_XDT_Y3LLB3_N0BMDTBM_RX_YQ = "anV0YnBvY2JueXB0YXBtcHFycnFybWxvanFkeXdtY3llb3N0bmdtbmRxYQ=="
    C_GJ1B_GHKE_GZWC2HOA3_B3A_WTM_YWPQA_W5NB_GXKA_GLWANH0A_HLIA_W9QA_WNPDM_JPDM54C_Q = "cGJ1bGhkeGZwc2hoa3B3aWtmYWpqaW5nbGxkaGlwanh0aHliaW9qaWNpdmJpdm54cQ=="
    D_GDM_Y2DLBM_ZUDM14B_HF5_ZNLIE_XBRE_G9K_ZXV4CMXHAN_VJD_GDVB_XFQE_GLID_XNRE_W1UC_GJIA_GTKBN_B5_YWPSCW = "dGdmY2dlbmZudm14bHF5ZnlieXBreG9kZXV4cmxhanVjdGdvbXFqeGlidXNreW1ucGJiaGtkbnB5YWpscw=="
    D_WTYAM_FVD_GTJB_W93B_XBP_ZWHXC_GFXB_HB1A2_ZR_ZW95E_HN1B2PVA_XVYAM_VRE_G9Z_Y2P2BMDYB_W10A_HV5A2LSC_W1T_Y2THBW = "dWtyamFvdGtjbW93bXBpZWhxcGFxbHB1a2ZrZW95eHN1b2pvaXVyamVreG9zY2p2bmdybW10aHV5a2lscW1tY2thbw=="
    E_HRHDN_FKA_XNX_ZQ = "eHRhdnFkaXNxZQ=="


@dataclass
class NistschemaSvIvAtomicBase64BinaryEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicBase64BinaryEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )