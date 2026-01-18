from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-1-NS"


class NistschemaSvIvAtomicBase64BinaryEnumeration1Type(Enum):
    ZM_FYAML5_ZM1I = b"farjiyfmb"
    D_HJH_ZWJMC3_ZHCG = b"traebfsvar"
    Y29ZA_XB5AMTV_ZNHWB2LPANHV_ZN_RRC_HVXA3_BYBN_BY_ZGHJE_HR3C2DQC_GRRDM_FQBM9SE_XHYE_HZZ_YN_FJ_ZM10 = b"cosipyjkofxpoiijxoftkpuqkprnprdhcxtwsgjpdkvajnolyxrxvsbqcfmt"
    B250_Z21MB2X5B_GLU_YMDUANDPBN_BWB3_V1_YWHQD2_NID_A = (
        b"ontgmfolylinbgnjwinppouuahjwcbt"
    )
    C3_RJB2XYCND2B_WPZA29WDMDJBNK = b"stcolrrwvmjskopvgcny"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-enumeration-1-NS"

    value: NistschemaSvIvAtomicBase64BinaryEnumeration1Type = field(
        metadata={
            "required": True,
            "format": "base64",
        }
    )
