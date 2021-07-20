from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-enumeration-2-NS"


class NistschemaSvIvListTimeEnumeration2Type(Enum):
    VALUE_02_07_10_05_21_31_17_09_51_08_01_04_13_14_56_11_19_09 = (
            XmlTime(2, 7, 10, 0),
            XmlTime(5, 21, 31, 0),
            XmlTime(17, 9, 51, 0),
            XmlTime(8, 1, 4, 0),
            XmlTime(13, 14, 56, 0),
            XmlTime(11, 19, 9, 0),
        )
    VALUE_02_37_40_01_35_46_22_26_57_11_17_46_07_27_09_01_54_28_03_54_13_16_15_01_10_04_55 = (
            XmlTime(2, 37, 40, 0),
            XmlTime(1, 35, 46, 0),
            XmlTime(22, 26, 57, 0),
            XmlTime(11, 17, 46, 0),
            XmlTime(7, 27, 9, 0),
            XmlTime(1, 54, 28, 0),
            XmlTime(3, 54, 13, 0),
            XmlTime(16, 15, 1, 0),
            XmlTime(10, 4, 55, 0),
        )
    VALUE_15_11_28_18_33_11_19_04_17_09_51_53_22_42_37_03_02_26_03_11_30_10_33_14_23_07_11 = (
            XmlTime(15, 11, 28, 0),
            XmlTime(18, 33, 11, 0),
            XmlTime(19, 4, 17, 0),
            XmlTime(9, 51, 53, 0),
            XmlTime(22, 42, 37, 0),
            XmlTime(3, 2, 26, 0),
            XmlTime(3, 11, 30, 0),
            XmlTime(10, 33, 14, 0),
            XmlTime(23, 7, 11, 0),
        )
    VALUE_00_31_28_16_04_13_21_19_12_20_41_05_13_09_11_13_30_17_15_11_31_13_53_26_15_25_17_23_25_22 = (
            XmlTime(0, 31, 28, 0),
            XmlTime(16, 4, 13, 0),
            XmlTime(21, 19, 12, 0),
            XmlTime(20, 41, 5, 0),
            XmlTime(13, 9, 11, 0),
            XmlTime(13, 30, 17, 0),
            XmlTime(15, 11, 31, 0),
            XmlTime(13, 53, 26, 0),
            XmlTime(15, 25, 17, 0),
            XmlTime(23, 25, 22, 0),
        )
    VALUE_19_35_00_21_44_32_01_01_06_20_00_57_12_53_40 = (
            XmlTime(19, 35, 0, 0),
            XmlTime(21, 44, 32, 0),
            XmlTime(1, 1, 6, 0),
            XmlTime(20, 0, 57, 0),
            XmlTime(12, 53, 40, 0),
        )
    VALUE_23_57_21_18_49_44_18_11_08_19_25_52_06_11_50_10_34_51 = (
            XmlTime(23, 57, 21, 0),
            XmlTime(18, 49, 44, 0),
            XmlTime(18, 11, 8, 0),
            XmlTime(19, 25, 52, 0),
            XmlTime(6, 11, 50, 0),
            XmlTime(10, 34, 51, 0),
        )
    VALUE_14_24_52_05_31_43_13_13_44_00_52_34_15_58_41 = (
            XmlTime(14, 24, 52, 0),
            XmlTime(5, 31, 43, 0),
            XmlTime(13, 13, 44, 0),
            XmlTime(0, 52, 34, 0),
            XmlTime(15, 58, 41, 0),
        )
    VALUE_23_12_14_02_15_55_08_50_43_01_59_11_01_45_29_22_01_06 = (
            XmlTime(23, 12, 14, 0),
            XmlTime(2, 15, 55, 0),
            XmlTime(8, 50, 43, 0),
            XmlTime(1, 59, 11, 0),
            XmlTime(1, 45, 29, 0),
            XmlTime(22, 1, 6, 0),
        )
    VALUE_02_44_16_12_25_01_03_56_20_02_01_01_02_46_01_11_45_00_03_36_58_07_44_35 = (
            XmlTime(2, 44, 16, 0),
            XmlTime(12, 25, 1, 0),
            XmlTime(3, 56, 20, 0),
            XmlTime(2, 1, 1, 0),
            XmlTime(2, 46, 1, 0),
            XmlTime(11, 45, 0, 0),
            XmlTime(3, 36, 58, 0),
            XmlTime(7, 44, 35, 0),
        )


@dataclass
class NistschemaSvIvListTimeEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-time-enumeration-2-NS"

    value: Optional[NistschemaSvIvListTimeEnumeration2Type] = field(
        default=None
    )
