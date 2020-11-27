from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-5-NS"


class NistschemaSvIvListGMonthDayEnumeration5Type(Enum):
    VALUE_08_12_06_25_07_14_05_27_07_26_12_22_09_25_08_28_09_05_02_23 = "--08-12 --06-25 --07-14 --05-27 --07-26 --12-22 --09-25 --08-28 --09-05 --02-23"
    VALUE_02_11_10_02_09_27_03_02_08_31_03_16_11_07_03_29_09_16 = "--02-11 --10-02 --09-27 --03-02 --08-31 --03-16 --11-07 --03-29 --09-16"
    VALUE_10_13_09_15_01_10_02_24_01_27_08_10_11_23 = "--10-13 --09-15 --01-10 --02-24 --01-27 --08-10 --11-23"
    VALUE_01_26_10_22_10_19_04_02_01_16_01_26_05_10_12_05 = "--01-26 --10-22 --10-19 --04-02 --01-16 --01-26 --05-10 --12-05"
    VALUE_09_25_08_01_01_26_06_24_03_21_02_10_06_26_06_06_03_28 = "--09-25 --08-01 --01-26 --06-24 --03-21 --02-10 --06-26 --06-06 --03-28"
    VALUE_10_05_07_14_10_13_07_11_06_05_12_19_07_02_12_30_07_05 = "--10-05 --07-14 --10-13 --07-11 --06-05 --12-19 --07-02 --12-30 --07-05"
    VALUE_12_06_06_20_06_24_10_01_07_20 = "--12-06 --06-20 --06-24 --10-01 --07-20"


@dataclass
class NistschemaSvIvListGMonthDayEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-5-NS"

    value: Optional[NistschemaSvIvListGMonthDayEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
