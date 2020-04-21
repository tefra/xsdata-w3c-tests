from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-4-NS"


class NistschemaSvIvListGMonthDayEnumeration4Type(Enum):
    """
    :cvar VALUE_05_11_06_11_07_22_05_17_02_01_09_18_05_01:
    :cvar VALUE_09_02_04_08_01_01_07_02_07_05:
    :cvar VALUE_09_16_02_01_09_05_01_17_02_04_10_11_05_27_03_01_04_26_09_02:
    :cvar VALUE_10_08_05_11_06_17_06_19_06_21_04_09_12_29:
    :cvar VALUE_10_30_09_02_01_03_08_15_09_07_12_28:
    :cvar VALUE_11_05_05_25_02_01_03_10_02_12:
    :cvar VALUE_11_23_09_21_06_05_04_28_08_06_04_16:
    """
    VALUE_05_11_06_11_07_22_05_17_02_01_09_18_05_01 = "--05-11 --06-11 --07-22 --05-17 --02-01 --09-18 --05-01"
    VALUE_09_02_04_08_01_01_07_02_07_05 = "--09-02 --04-08 --01-01 --07-02 --07-05"
    VALUE_09_16_02_01_09_05_01_17_02_04_10_11_05_27_03_01_04_26_09_02 = "--09-16 --02-01 --09-05 --01-17 --02-04 --10-11 --05-27 --03-01 --04-26 --09-02"
    VALUE_10_08_05_11_06_17_06_19_06_21_04_09_12_29 = "--10-08 --05-11 --06-17 --06-19 --06-21 --04-09 --12-29"
    VALUE_10_30_09_02_01_03_08_15_09_07_12_28 = "--10-30 --09-02 --01-03 --08-15 --09-07 --12-28"
    VALUE_11_05_05_25_02_01_03_10_02_12 = "--11-05 --05-25 --02-01 --03-10 --02-12"
    VALUE_11_23_09_21_06_05_04_28_08_06_04_16 = "--11-23 --09-21 --06-05 --04-28 --08-06 --04-16"


@dataclass
class NistschemaSvIvListGMonthDayEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-4-NS"

    value: Optional[NistschemaSvIvListGMonthDayEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
