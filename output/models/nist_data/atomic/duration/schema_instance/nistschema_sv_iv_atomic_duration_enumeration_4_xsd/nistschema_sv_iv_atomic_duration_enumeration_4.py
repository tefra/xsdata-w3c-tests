from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-enumeration-4-NS"


class NistschemaSvIvAtomicDurationEnumeration4Type(Enum):
    P2025_Y05_M27_DT08_H26_M21_S = XmlDuration("P2025Y05M27DT08H26M21S")
    P1992_Y12_M03_DT11_H54_M34_S = XmlDuration("P1992Y12M03DT11H54M34S")
    P2006_Y06_M20_DT01_H05_M49_S = XmlDuration("P2006Y06M20DT01H05M49S")
    P2007_Y02_M04_DT05_H26_M40_S = XmlDuration("P2007Y02M04DT05H26M40S")
    P1978_Y02_M20_DT15_H18_M23_S = XmlDuration("P1978Y02M20DT15H18M23S")
    P2017_Y06_M28_DT06_H31_M49_S = XmlDuration("P2017Y06M28DT06H31M49S")
    P2025_Y04_M14_DT05_H33_M34_S = XmlDuration("P2025Y04M14DT05H33M34S")


@dataclass
class NistschemaSvIvAtomicDurationEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicDurationEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
