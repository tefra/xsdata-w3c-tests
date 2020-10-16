from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-3-NS"


class NistschemaSvIvListGMonthEnumeration3Type(Enum):
    """
    :cvar VALUE_10_06_07_10_02_04_07:
    :cvar VALUE_12_04_08_08_08_08_04:
    :cvar VALUE_09_04_02_12_08_03_02_01:
    :cvar VALUE_02_11_06_07_02_08_01_06_07:
    :cvar VALUE_02_05_10_03_09_02_04_09:
    :cvar VALUE_12_10_12_09_09_04_04:
    :cvar VALUE_11_02_02_05_10_05:
    :cvar VALUE_02_05_09_09_02_04:
    :cvar VALUE_04_03_02_06_06_06_08:
    :cvar VALUE_04_08_03_06_10:
    """
    VALUE_10_06_07_10_02_04_07 = "--10 --06 --07 --10 --02 --04 --07"
    VALUE_12_04_08_08_08_08_04 = "--12 --04 --08 --08 --08 --08 --04"
    VALUE_09_04_02_12_08_03_02_01 = "--09 --04 --02 --12 --08 --03 --02 --01"
    VALUE_02_11_06_07_02_08_01_06_07 = "--02 --11 --06 --07 --02 --08 --01 --06 --07"
    VALUE_02_05_10_03_09_02_04_09 = "--02 --05 --10 --03 --09 --02 --04 --09"
    VALUE_12_10_12_09_09_04_04 = "--12 --10 --12 --09 --09 --04 --04"
    VALUE_11_02_02_05_10_05 = "--11 --02 --02 --05 --10 --05"
    VALUE_02_05_09_09_02_04 = "--02 --05 --09 --09 --02 --04"
    VALUE_04_03_02_06_06_06_08 = "--04 --03 --02 --06 --06 --06 --08"
    VALUE_04_08_03_06_10 = "--04 --08 --03 --06 --10"


@dataclass
class NistschemaSvIvListGMonthEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-3-NS"

    value: Optional[NistschemaSvIvListGMonthEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
