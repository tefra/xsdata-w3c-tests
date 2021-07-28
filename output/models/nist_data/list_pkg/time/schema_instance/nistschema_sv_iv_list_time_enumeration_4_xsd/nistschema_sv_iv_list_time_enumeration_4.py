from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-enumeration-4-NS"


class NistschemaSvIvListTimeEnumeration4Type(Enum):
    VALUE_20_55_32_13_12_24_05_09_54_15_26_04_21_18_52_07_04_22_13_43_48 = (
            XmlTime(20, 55, 32, 0),
            XmlTime(13, 12, 24, 0),
            XmlTime(5, 9, 54, 0),
            XmlTime(15, 26, 4, 0),
            XmlTime(21, 18, 52, 0),
            XmlTime(7, 4, 22, 0),
            XmlTime(13, 43, 48, 0),
        )
    VALUE_21_26_26_11_23_05_22_27_57_02_41_13_12_19_00_18_13_44 = (
            XmlTime(21, 26, 26, 0),
            XmlTime(11, 23, 5, 0),
            XmlTime(22, 27, 57, 0),
            XmlTime(2, 41, 13, 0),
            XmlTime(12, 19, 0, 0),
            XmlTime(18, 13, 44, 0),
        )
    VALUE_07_27_57_09_04_49_17_05_01_12_15_48_01_00_58_10_04_48 = (
            XmlTime(7, 27, 57, 0),
            XmlTime(9, 4, 49, 0),
            XmlTime(17, 5, 1, 0),
            XmlTime(12, 15, 48, 0),
            XmlTime(1, 0, 58, 0),
            XmlTime(10, 4, 48, 0),
        )
    VALUE_23_21_47_07_35_16_02_59_18_22_55_26_02_20_03 = (
            XmlTime(23, 21, 47, 0),
            XmlTime(7, 35, 16, 0),
            XmlTime(2, 59, 18, 0),
            XmlTime(22, 55, 26, 0),
            XmlTime(2, 20, 3, 0),
        )
    VALUE_08_08_33_21_55_09_10_27_06_14_09_32_22_18_18_11_48_00_11_07_55_14_18_46_16_46_53_14_53_55 = (
            XmlTime(8, 8, 33, 0),
            XmlTime(21, 55, 9, 0),
            XmlTime(10, 27, 6, 0),
            XmlTime(14, 9, 32, 0),
            XmlTime(22, 18, 18, 0),
            XmlTime(11, 48, 0, 0),
            XmlTime(11, 7, 55, 0),
            XmlTime(14, 18, 46, 0),
            XmlTime(16, 46, 53, 0),
            XmlTime(14, 53, 55, 0),
        )
    VALUE_23_33_25_12_19_16_03_56_40_07_24_55_21_32_06_11_28_14_20_10_08_14_11_43 = (
            XmlTime(23, 33, 25, 0),
            XmlTime(12, 19, 16, 0),
            XmlTime(3, 56, 40, 0),
            XmlTime(7, 24, 55, 0),
            XmlTime(21, 32, 6, 0),
            XmlTime(11, 28, 14, 0),
            XmlTime(20, 10, 8, 0),
            XmlTime(14, 11, 43, 0),
        )
    VALUE_09_02_38_04_10_17_21_01_45_10_23_34_07_06_37_06_19_51_06_20_06_19_54_42_12_23_53 = (
            XmlTime(9, 2, 38, 0),
            XmlTime(4, 10, 17, 0),
            XmlTime(21, 1, 45, 0),
            XmlTime(10, 23, 34, 0),
            XmlTime(7, 6, 37, 0),
            XmlTime(6, 19, 51, 0),
            XmlTime(6, 20, 6, 0),
            XmlTime(19, 54, 42, 0),
            XmlTime(12, 23, 53, 0),
        )
    VALUE_14_33_48_01_19_39_07_15_06_05_12_11_21_08_03_03_02_34_04_16_29_09_27_29_19_36_04_09_00_20 = (
            XmlTime(14, 33, 48, 0),
            XmlTime(1, 19, 39, 0),
            XmlTime(7, 15, 6, 0),
            XmlTime(5, 12, 11, 0),
            XmlTime(21, 8, 3, 0),
            XmlTime(3, 2, 34, 0),
            XmlTime(4, 16, 29, 0),
            XmlTime(9, 27, 29, 0),
            XmlTime(19, 36, 4, 0),
            XmlTime(9, 0, 20, 0),
        )
    VALUE_04_52_05_18_26_53_04_51_11_01_39_09_16_03_11_15_17_05_03_31_28_14_31_06 = (
            XmlTime(4, 52, 5, 0),
            XmlTime(18, 26, 53, 0),
            XmlTime(4, 51, 11, 0),
            XmlTime(1, 39, 9, 0),
            XmlTime(16, 3, 11, 0),
            XmlTime(15, 17, 5, 0),
            XmlTime(3, 31, 28, 0),
            XmlTime(14, 31, 6, 0),
        )
    VALUE_10_19_34_00_35_24_17_00_23_17_00_38_16_54_19_19_35_48_15_15_24_00_09_08_16_23_31 = (
            XmlTime(10, 19, 34, 0),
            XmlTime(0, 35, 24, 0),
            XmlTime(17, 0, 23, 0),
            XmlTime(17, 0, 38, 0),
            XmlTime(16, 54, 19, 0),
            XmlTime(19, 35, 48, 0),
            XmlTime(15, 15, 24, 0),
            XmlTime(0, 9, 8, 0),
            XmlTime(16, 23, 31, 0),
        )


@dataclass
class NistschemaSvIvListTimeEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-time-enumeration-4-NS"

    value: Optional[NistschemaSvIvListTimeEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
