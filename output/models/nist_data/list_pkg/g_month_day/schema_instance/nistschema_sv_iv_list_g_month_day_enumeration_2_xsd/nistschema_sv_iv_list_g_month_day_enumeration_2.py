from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-2-NS"


class NistschemaSvIvListGMonthDayEnumeration2Type(Enum):
    """
    :cvar VALUE_01_24_09_05_09_29_04_28_10_01:
    :cvar VALUE_03_18_12_15_06_19_12_09_01_28:
    :cvar VALUE_03_21_11_21_03_15_03_20_12_13_10_26_11_15:
    :cvar VALUE_06_08_03_26_03_22_01_27_03_20_06_08_01_10_07_17_03_02:
    :cvar VALUE_07_24_08_04_10_05_11_19_08_05_03_06_10_17_08_11:
    :cvar VALUE_08_01_05_03_12_09_08_13_09_10_01_09_11_06_03_07_01_28:
    :cvar VALUE_11_10_03_26_08_04_12_23_02_11_06_02_08_06_07_10_05_18_08_10:
    :cvar VALUE_11_16_10_05_04_18_09_19_11_13_05_03_06_13_02_25:
    """
    VALUE_01_24_09_05_09_29_04_28_10_01 = "--01-24 --09-05 --09-29 --04-28 --10-01"
    VALUE_03_18_12_15_06_19_12_09_01_28 = "--03-18 --12-15 --06-19 --12-09 --01-28"
    VALUE_03_21_11_21_03_15_03_20_12_13_10_26_11_15 = "--03-21 --11-21 --03-15 --03-20 --12-13 --10-26 --11-15"
    VALUE_06_08_03_26_03_22_01_27_03_20_06_08_01_10_07_17_03_02 = "--06-08 --03-26 --03-22 --01-27 --03-20 --06-08 --01-10 --07-17 --03-02"
    VALUE_07_24_08_04_10_05_11_19_08_05_03_06_10_17_08_11 = "--07-24 --08-04 --10-05 --11-19 --08-05 --03-06 --10-17 --08-11"
    VALUE_08_01_05_03_12_09_08_13_09_10_01_09_11_06_03_07_01_28 = "--08-01 --05-03 --12-09 --08-13 --09-10 --01-09 --11-06 --03-07 --01-28"
    VALUE_11_10_03_26_08_04_12_23_02_11_06_02_08_06_07_10_05_18_08_10 = "--11-10 --03-26 --08-04 --12-23 --02-11 --06-02 --08-06 --07-10 --05-18 --08-10"
    VALUE_11_16_10_05_04_18_09_19_11_13_05_03_06_13_02_25 = "--11-16 --10-05 --04-18 --09-19 --11-13 --05-03 --06-13 --02-25"


@dataclass
class NistschemaSvIvListGMonthDayEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-2-NS"

    value: Optional[NistschemaSvIvListGMonthDayEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )