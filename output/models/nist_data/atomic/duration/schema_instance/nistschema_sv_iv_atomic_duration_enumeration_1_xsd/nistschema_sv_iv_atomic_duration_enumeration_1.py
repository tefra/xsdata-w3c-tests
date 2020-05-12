from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-enumeration-1-NS"


class NistschemaSvIvAtomicDurationEnumeration1Type(Enum):
    """
    :cvar P2025_Y01_M14_DT13_H56_M25_S:
    :cvar P1983_Y03_M24_DT09_H12_M25_S:
    :cvar P1984_Y01_M10_DT20_H37_M24_S:
    :cvar P1997_Y09_M21_DT02_H26_M51_S:
    :cvar P1988_Y07_M27_DT12_H21_M55_S:
    :cvar P2000_Y08_M25_DT00_H50_M37_S:
    :cvar P1981_Y11_M06_DT01_H43_M46_S:
    :cvar P1982_Y04_M25_DT04_H30_M00_S:
    :cvar P2011_Y03_M13_DT10_H22_M00_S:
    """
    P2025_Y01_M14_DT13_H56_M25_S = "P2025Y01M14DT13H56M25S"
    P1983_Y03_M24_DT09_H12_M25_S = "P1983Y03M24DT09H12M25S"
    P1984_Y01_M10_DT20_H37_M24_S = "P1984Y01M10DT20H37M24S"
    P1997_Y09_M21_DT02_H26_M51_S = "P1997Y09M21DT02H26M51S"
    P1988_Y07_M27_DT12_H21_M55_S = "P1988Y07M27DT12H21M55S"
    P2000_Y08_M25_DT00_H50_M37_S = "P2000Y08M25DT00H50M37S"
    P1981_Y11_M06_DT01_H43_M46_S = "P1981Y11M06DT01H43M46S"
    P1982_Y04_M25_DT04_H30_M00_S = "P1982Y04M25DT04H30M00S"
    P2011_Y03_M13_DT10_H22_M00_S = "P2011Y03M13DT10H22M00S"


@dataclass
class NistschemaSvIvAtomicDurationEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicDurationEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
