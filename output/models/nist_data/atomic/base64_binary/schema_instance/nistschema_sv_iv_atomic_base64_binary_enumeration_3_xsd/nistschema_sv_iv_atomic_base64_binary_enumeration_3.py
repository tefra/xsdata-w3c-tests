from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-3-NS"


class NistschemaSvIvAtomicBase64BinaryEnumeration3Type(Enum):
    """
    :cvar YN_VUAN_VX_ZNH0A_XHZ_YMPJE_HFMC_XNXD3LR_YMTJDN_RRD2LQB_XH3A_G9XDMPHDN_VNAMPKE_WDND_GX1D_XBZ_YMLNAN_Y:
    :cvar YN_Z0C_GVZ_YXLW_Z2LVC3_NO_YWZOD_WNXB3_B1C_GT5_Y2_NUD_GPUE_XLHD29WD_XFH_Y25Q_ZXL1DM5YD_GFN:
    :cvar C_XNRA_WVX_YWN1_ZXH5B3_F0DM_RN_Z2_ZNB_GL2E_GRSD_GK:
    :cvar CN_VIA21P_Z3D3C_WF5D_HLV_ZGTR_Y2TV_ZXF4DM_RK_ZMTH_ZM_NWAMP1_ZGRVC_GRRDNDN_ZN_JMD_GTTDN_VO_Z3_I:
    :cvar CN_VM_ZGRUC_WV5C3_ZS_Z2_ZZD_GVY_ZHLYB2_VTA_GFTB211C_G50E_HN3:
    :cvar E_GJJE_XJJB_HVJC_XJLB_HZHBM_RZAMTHCMPRB_XZYD_GV4_Z3HO_ZXZTC_XZ0BMX0DNH4D_GRVD2_ZXCMTQ_Y2S:
    """
    YN_VUAN_VX_ZNH0A_XHZ_YMPJE_HFMC_XNXD3LR_YMTJDN_RRD2LQB_XH3A_G9XDMPHDN_VNAMPKE_WDND_GX1D_XBZ_YMLNAN_Y = "YnVuanVxZnh0aXhzYmpjeHFmcXNxd3lrYmtjdnRrd2lqbXh3aG9xdmphdnVnampkeWdndGx1dXBzYmlnanY="
    YN_Z0C_GVZ_YXLW_Z2LVC3_NO_YWZOD_WNXB3_B1C_GT5_Y2_NUD_GPUE_XLHD29WD_XFH_Y25Q_ZXL1DM5YD_GFN = "YnZ0cGVzYXlwZ2lvc3NoYWZodWNxb3B1cGt5Y2NudGpueXlhd29wdXFhY25qZXl1dm5ydGFn"
    C_XNRA_WVX_YWN1_ZXH5B3_F0DM_RN_Z2_ZNB_GL2E_GRSD_GK = "cXNraWVxYWN1ZXh5b3F0dmRnZ2ZnbGl2eGRsdGk="
    CN_VIA21P_Z3D3C_WF5D_HLV_ZGTR_Y2TV_ZXF4DM_RK_ZMTH_ZM_NWAMP1_ZGRVC_GRRDNDN_ZN_JMD_GTTDN_VO_Z3_I = "cnVia21pZ3d3cWF5dHlvZGtrY2tvZXF4dmRkZmthZmNwamp1ZGRvcGRrdndnZnJmdGttdnVoZ3I="
    CN_VM_ZGRUC_WV5C3_ZS_Z2_ZZD_GVY_ZHLYB2_VTA_GFTB211C_G50E_HN3 = "cnVmZGRucWV5c3ZsZ2ZzdGVyZHlyb2VtaGFtb211cG50eHN3"
    E_GJJE_XJJB_HVJC_XJLB_HZHBM_RZAMTHCMPRB_XZYD_GV4_Z3HO_ZXZTC_XZ0BMX0DNH4D_GRVD2_ZXCMTQ_Y2S = "eGJjeXJjbHVjcXJlbHZhbmRzamthcmprbXZydGV4Z3hoZXZtcXZ0bmx0dnh4dGRvd2ZxcmtqY2s="


@dataclass
class NistschemaSvIvAtomicBase64BinaryEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicBase64BinaryEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )