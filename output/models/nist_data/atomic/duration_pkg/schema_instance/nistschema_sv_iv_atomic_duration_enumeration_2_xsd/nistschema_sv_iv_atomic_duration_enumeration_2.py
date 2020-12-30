from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-enumeration-2-NS"


class NistschemaSvIvAtomicDurationEnumeration2Type(Enum):
    P2030_Y06_M26_DT21_H55_M47_S = Duration("P2030Y06M26DT21H55M47S")
    P1979_Y03_M06_DT16_H39_M48_S = Duration("P1979Y03M06DT16H39M48S")
    P1987_Y06_M06_DT18_H56_M03_S = Duration("P1987Y06M06DT18H56M03S")
    P1977_Y04_M02_DT05_H48_M43_S = Duration("P1977Y04M02DT05H48M43S")
    P1995_Y02_M01_DT05_H15_M19_S = Duration("P1995Y02M01DT05H15M19S")
    P2019_Y06_M07_DT15_H23_M38_S = Duration("P2019Y06M07DT15H23M38S")
    P1976_Y12_M13_DT09_H35_M31_S = Duration("P1976Y12M13DT09H35M31S")
    P1989_Y03_M16_DT04_H44_M26_S = Duration("P1989Y03M16DT04H44M26S")
    P1993_Y12_M14_DT04_H03_M02_S = Duration("P1993Y12M14DT04H03M02S")


@dataclass
class NistschemaSvIvAtomicDurationEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicDurationEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
