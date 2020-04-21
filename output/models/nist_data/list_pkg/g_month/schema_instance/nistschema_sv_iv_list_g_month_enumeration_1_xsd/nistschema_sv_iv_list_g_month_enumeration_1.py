from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-1-NS"


class NistschemaSvIvListGMonthEnumeration1Type(Enum):
    """
    :cvar VALUE_02_09_10_11_06_05_02:
    :cvar VALUE_05_08_11_05_10_06_09_01_05_12:
    :cvar VALUE_05_09_10_05_10_12_04:
    :cvar VALUE_06_05_10_06_04_06_07_04_09_03:
    :cvar VALUE_08_08_07_02_01_04_02_11_01_11:
    :cvar VALUE_10_09_07_07_09_08_09:
    :cvar VALUE_11_03_09_08_05_09_02_06_04:
    """
    VALUE_02_09_10_11_06_05_02 = "--02 --09 --10 --11 --06 --05 --02"
    VALUE_05_08_11_05_10_06_09_01_05_12 = "--05 --08 --11 --05 --10 --06 --09 --01 --05 --12"
    VALUE_05_09_10_05_10_12_04 = "--05 --09 --10 --05 --10 --12 --04"
    VALUE_06_05_10_06_04_06_07_04_09_03 = "--06 --05 --10 --06 --04 --06 --07 --04 --09 --03"
    VALUE_08_08_07_02_01_04_02_11_01_11 = "--08 --08 --07 --02 --01 --04 --02 --11 --01 --11"
    VALUE_10_09_07_07_09_08_09 = "--10 --09 --07 --07 --09 --08 --09"
    VALUE_11_03_09_08_05_09_02_06_04 = "--11 --03 --09 --08 --05 --09 --02 --06 --04"


@dataclass
class NistschemaSvIvListGMonthEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvListGMonthEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
