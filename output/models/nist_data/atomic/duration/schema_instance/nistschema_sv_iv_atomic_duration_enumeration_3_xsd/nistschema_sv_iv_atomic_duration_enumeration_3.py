from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-enumeration-3-NS"


class NistschemaSvIvAtomicDurationEnumeration3Type(Enum):
    P2014_Y02_M13_DT07_H57_M16_S = XmlDuration("P2014Y02M13DT07H57M16S")
    P1971_Y01_M25_DT00_H00_M13_S = XmlDuration("P1971Y01M25DT00H00M13S")
    P1992_Y03_M13_DT23_H32_M32_S = XmlDuration("P1992Y03M13DT23H32M32S")
    P1999_Y01_M17_DT20_H04_M34_S = XmlDuration("P1999Y01M17DT20H04M34S")
    P1974_Y07_M30_DT07_H58_M46_S = XmlDuration("P1974Y07M30DT07H58M46S")
    P1979_Y12_M12_DT13_H36_M50_S = XmlDuration("P1979Y12M12DT13H36M50S")
    P2018_Y05_M02_DT20_H30_M41_S = XmlDuration("P2018Y05M02DT20H30M41S")
    P2005_Y11_M15_DT09_H43_M12_S = XmlDuration("P2005Y11M15DT09H43M12S")
    P1995_Y06_M08_DT02_H47_M24_S = XmlDuration("P1995Y06M08DT02H47M24S")
    P1973_Y07_M23_DT17_H25_M15_S = XmlDuration("P1973Y07M23DT17H25M15S")


@dataclass
class NistschemaSvIvAtomicDurationEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicDurationEnumeration3Type] = field(
        default=None
    )
