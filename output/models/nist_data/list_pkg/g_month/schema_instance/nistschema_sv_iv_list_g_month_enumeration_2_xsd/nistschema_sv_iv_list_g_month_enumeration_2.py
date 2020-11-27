from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-2-NS"


class NistschemaSvIvListGMonthEnumeration2Type(Enum):
    VALUE_12_08_08_06_08_11_09_12_05_09 = "--12 --08 --08 --06 --08 --11 --09 --12 --05 --09"
    VALUE_06_10_10_08_07_07_04_11_02 = "--06 --10 --10 --08 --07 --07 --04 --11 --02"
    VALUE_09_09_09_06_01_04_01_09 = "--09 --09 --09 --06 --01 --04 --01 --09"
    VALUE_06_11_11_06_02_04_01_05_06 = "--06 --11 --11 --06 --02 --04 --01 --05 --06"
    VALUE_07_08_01_06_07 = "--07 --08 --01 --06 --07"
    VALUE_11_07_12_09_09_09_01_10 = "--11 --07 --12 --09 --09 --09 --01 --10"
    VALUE_02_08_08_07_02_09_02 = "--02 --08 --08 --07 --02 --09 --02"
    VALUE_05_04_01_03_11_04_01_10_06 = "--05 --04 --01 --03 --11 --04 --01 --10 --06"


@dataclass
class NistschemaSvIvListGMonthEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-2-NS"

    value: Optional[NistschemaSvIvListGMonthEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
