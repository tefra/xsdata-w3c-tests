from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-5-NS"


class NistschemaSvIvListGMonthEnumeration5Type(Enum):
    """
    :cvar VALUE_03_02_01_05_08_04_02_07:
    :cvar VALUE_03_09_07_07_10_07_08_11_08_03:
    :cvar VALUE_04_05_04_10_06_08_03:
    :cvar VALUE_07_12_12_03_01_11_01_05_03:
    :cvar VALUE_11_07_07_02_06_02:
    :cvar VALUE_11_11_04_09_03_10_05_03:
    """
    VALUE_03_02_01_05_08_04_02_07 = "--03 --02 --01 --05 --08 --04 --02 --07"
    VALUE_03_09_07_07_10_07_08_11_08_03 = "--03 --09 --07 --07 --10 --07 --08 --11 --08 --03"
    VALUE_04_05_04_10_06_08_03 = "--04 --05 --04 --10 --06 --08 --03"
    VALUE_07_12_12_03_01_11_01_05_03 = "--07 --12 --12 --03 --01 --11 --01 --05 --03"
    VALUE_11_07_07_02_06_02 = "--11 --07 --07 --02 --06 --02"
    VALUE_11_11_04_09_03_10_05_03 = "--11 --11 --04 --09 --03 --10 --05 --03"


@dataclass
class NistschemaSvIvListGMonthEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-5-NS"

    value: Optional[NistschemaSvIvListGMonthEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
