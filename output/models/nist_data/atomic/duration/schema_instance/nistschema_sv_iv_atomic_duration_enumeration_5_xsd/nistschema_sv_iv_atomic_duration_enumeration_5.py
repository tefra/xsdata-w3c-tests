from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-enumeration-5-NS"


class NistschemaSvIvAtomicDurationEnumeration5Type(Enum):
    """
    :cvar P1970_Y01_M27_DT04_H00_M33_S:
    :cvar P1974_Y01_M22_DT17_H35_M48_S:
    :cvar P1987_Y03_M14_DT08_H37_M46_S:
    :cvar P1995_Y02_M03_DT12_H24_M43_S:
    :cvar P2002_Y03_M13_DT22_H40_M25_S:
    :cvar P2002_Y11_M07_DT03_H22_M59_S:
    :cvar P2004_Y09_M11_DT17_H07_M38_S:
    :cvar P2012_Y01_M30_DT22_H51_M53_S:
    :cvar P2024_Y05_M28_DT11_H34_M44_S:
    """
    P1970_Y01_M27_DT04_H00_M33_S = "P1970Y01M27DT04H00M33S"
    P1974_Y01_M22_DT17_H35_M48_S = "P1974Y01M22DT17H35M48S"
    P1987_Y03_M14_DT08_H37_M46_S = "P1987Y03M14DT08H37M46S"
    P1995_Y02_M03_DT12_H24_M43_S = "P1995Y02M03DT12H24M43S"
    P2002_Y03_M13_DT22_H40_M25_S = "P2002Y03M13DT22H40M25S"
    P2002_Y11_M07_DT03_H22_M59_S = "P2002Y11M07DT03H22M59S"
    P2004_Y09_M11_DT17_H07_M38_S = "P2004Y09M11DT17H07M38S"
    P2012_Y01_M30_DT22_H51_M53_S = "P2012Y01M30DT22H51M53S"
    P2024_Y05_M28_DT11_H34_M44_S = "P2024Y05M28DT11H34M44S"


@dataclass
class NistschemaSvIvAtomicDurationEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-duration-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicDurationEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
