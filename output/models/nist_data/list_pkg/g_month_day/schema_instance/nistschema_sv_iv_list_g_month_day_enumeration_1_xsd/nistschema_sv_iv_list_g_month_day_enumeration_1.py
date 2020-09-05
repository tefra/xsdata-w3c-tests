from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-1-NS"


class NistschemaSvIvListGMonthDayEnumeration1Type(Enum):
    """
    :cvar VALUE_06_15_07_19_03_23_06_10_12_07_06_12_08_06_09_17_11_15:
    :cvar VALUE_12_07_05_06_01_17_07_12_06_06_01_14_06_01:
    :cvar VALUE_02_09_06_03_07_04_12_24_04_02_03_30_09_13_09_09_07_10:
    :cvar VALUE_10_18_07_17_11_11_11_02_06_17_02_05:
    :cvar VALUE_07_14_04_06_01_18_10_07_06_24_03_18_08_20_10_15_07_13:
    :cvar VALUE_01_07_08_03_01_20_10_28_03_21_02_07_01_14_01_11:
    """
    VALUE_06_15_07_19_03_23_06_10_12_07_06_12_08_06_09_17_11_15 = "--06-15 --07-19 --03-23 --06-10 --12-07 --06-12 --08-06 --09-17 --11-15"
    VALUE_12_07_05_06_01_17_07_12_06_06_01_14_06_01 = "--12-07 --05-06 --01-17 --07-12 --06-06 --01-14 --06-01"
    VALUE_02_09_06_03_07_04_12_24_04_02_03_30_09_13_09_09_07_10 = "--02-09 --06-03 --07-04 --12-24 --04-02 --03-30 --09-13 --09-09 --07-10"
    VALUE_10_18_07_17_11_11_11_02_06_17_02_05 = "--10-18 --07-17 --11-11 --11-02 --06-17 --02-05"
    VALUE_07_14_04_06_01_18_10_07_06_24_03_18_08_20_10_15_07_13 = "--07-14 --04-06 --01-18 --10-07 --06-24 --03-18 --08-20 --10-15 --07-13"
    VALUE_01_07_08_03_01_20_10_28_03_21_02_07_01_14_01_11 = "--01-07 --08-03 --01-20 --10-28 --03-21 --02-07 --01-14 --01-11"


@dataclass
class NistschemaSvIvListGMonthDayEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-1-NS"

    value: Optional[NistschemaSvIvListGMonthDayEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
