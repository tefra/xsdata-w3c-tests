from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-3-NS"


class NistschemaSvIvListGMonthDayEnumeration3Type(Enum):
    VALUE_10_27_08_13_07_15_02_01_01_16_06_17_10_05_01_21 = "--10-27 --08-13 --07-15 --02-01 --01-16 --06-17 --10-05 --01-21"
    VALUE_11_15_12_29_10_05_05_21_03_08_05_29 = "--11-15 --12-29 --10-05 --05-21 --03-08 --05-29"
    VALUE_06_29_01_23_07_14_09_22_02_24_01_05 = "--06-29 --01-23 --07-14 --09-22 --02-24 --01-05"
    VALUE_04_08_03_18_05_15_08_27_04_28_01_27_11_13_08_28 = "--04-08 --03-18 --05-15 --08-27 --04-28 --01-27 --11-13 --08-28"
    VALUE_09_13_06_20_03_06_09_19_04_02_11_23 = "--09-13 --06-20 --03-06 --09-19 --04-02 --11-23"
    VALUE_06_11_11_05_08_18_09_11_05_29_08_21_09_10_10_14 = "--06-11 --11-05 --08-18 --09-11 --05-29 --08-21 --09-10 --10-14"


@dataclass
class NistschemaSvIvListGMonthDayEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-3-NS"

    value: Optional[NistschemaSvIvListGMonthDayEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
