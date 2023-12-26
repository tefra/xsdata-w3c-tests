from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-enumeration-1-NS"


class NistschemaSvIvListTimeEnumeration1Type(Enum):
    VALUE_16_22_20_01_19_11_21_37_24_12_13_13_14_56_46_19_02_14 = (
        XmlTime(16, 22, 20, 0),
        XmlTime(1, 19, 11, 0),
        XmlTime(21, 37, 24, 0),
        XmlTime(12, 13, 13, 0),
        XmlTime(14, 56, 46, 0),
        XmlTime(19, 2, 14, 0),
    )
    VALUE_07_17_31_13_47_35_14_07_26_07_08_30_15_18_40_09_10_42 = (
        XmlTime(7, 17, 31, 0),
        XmlTime(13, 47, 35, 0),
        XmlTime(14, 7, 26, 0),
        XmlTime(7, 8, 30, 0),
        XmlTime(15, 18, 40, 0),
        XmlTime(9, 10, 42, 0),
    )
    VALUE_18_10_11_22_21_23_23_58_22_17_08_12_08_14_52_00_17_12_03_05_44_20_23_12_19_52_22_06_09_32 = (
        XmlTime(18, 10, 11, 0),
        XmlTime(22, 21, 23, 0),
        XmlTime(23, 58, 22, 0),
        XmlTime(17, 8, 12, 0),
        XmlTime(8, 14, 52, 0),
        XmlTime(0, 17, 12, 0),
        XmlTime(3, 5, 44, 0),
        XmlTime(20, 23, 12, 0),
        XmlTime(19, 52, 22, 0),
        XmlTime(6, 9, 32, 0),
    )
    VALUE_21_21_52_03_24_38_12_34_13_20_23_03_05_52_11_11_36_11_01_00_51 = (
        XmlTime(21, 21, 52, 0),
        XmlTime(3, 24, 38, 0),
        XmlTime(12, 34, 13, 0),
        XmlTime(20, 23, 3, 0),
        XmlTime(5, 52, 11, 0),
        XmlTime(11, 36, 11, 0),
        XmlTime(1, 0, 51, 0),
    )
    VALUE_17_14_09_06_52_14_10_05_58_17_05_37_22_36_07 = (
        XmlTime(17, 14, 9, 0),
        XmlTime(6, 52, 14, 0),
        XmlTime(10, 5, 58, 0),
        XmlTime(17, 5, 37, 0),
        XmlTime(22, 36, 7, 0),
    )
    VALUE_07_57_55_14_57_18_15_27_38_20_24_52_05_27_55 = (
        XmlTime(7, 57, 55, 0),
        XmlTime(14, 57, 18, 0),
        XmlTime(15, 27, 38, 0),
        XmlTime(20, 24, 52, 0),
        XmlTime(5, 27, 55, 0),
    )
    VALUE_02_50_34_03_25_09_15_41_25_13_28_11_12_21_19_05_03_58_08_08_30_01_14_08_18_54_43 = (
        XmlTime(2, 50, 34, 0),
        XmlTime(3, 25, 9, 0),
        XmlTime(15, 41, 25, 0),
        XmlTime(13, 28, 11, 0),
        XmlTime(12, 21, 19, 0),
        XmlTime(5, 3, 58, 0),
        XmlTime(8, 8, 30, 0),
        XmlTime(1, 14, 8, 0),
        XmlTime(18, 54, 43, 0),
    )


@dataclass
class NistschemaSvIvListTimeEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-time-enumeration-1-NS"

    value: Optional[NistschemaSvIvListTimeEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
