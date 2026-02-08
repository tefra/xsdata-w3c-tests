from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-enumeration-3-NS"


class NistschemaSvIvListTimeEnumeration3Type(Enum):
    VALUE_02_36_41_22_58_23_23_54_34_17_47_57_16_03_44_11_16_31 = (
        XmlTime(2, 36, 41, 0),
        XmlTime(22, 58, 23, 0),
        XmlTime(23, 54, 34, 0),
        XmlTime(17, 47, 57, 0),
        XmlTime(16, 3, 44, 0),
        XmlTime(11, 16, 31, 0),
    )
    VALUE_22_25_13_04_11_03_02_21_03_00_27_00_12_22_59_13_27_00 = (
        XmlTime(22, 25, 13, 0),
        XmlTime(4, 11, 3, 0),
        XmlTime(2, 21, 3, 0),
        XmlTime(0, 27, 0, 0),
        XmlTime(12, 22, 59, 0),
        XmlTime(13, 27, 0, 0),
    )
    VALUE_03_39_31_00_47_50_20_17_03_14_41_39_06_09_20_08_41_05_16_54_31_05_52_59 = (
        XmlTime(3, 39, 31, 0),
        XmlTime(0, 47, 50, 0),
        XmlTime(20, 17, 3, 0),
        XmlTime(14, 41, 39, 0),
        XmlTime(6, 9, 20, 0),
        XmlTime(8, 41, 5, 0),
        XmlTime(16, 54, 31, 0),
        XmlTime(5, 52, 59, 0),
    )
    VALUE_19_45_50_05_32_23_12_42_04_16_34_52_20_20_25_17_26_01_04_07_14_16_43_46_18_17_58 = (
        XmlTime(19, 45, 50, 0),
        XmlTime(5, 32, 23, 0),
        XmlTime(12, 42, 4, 0),
        XmlTime(16, 34, 52, 0),
        XmlTime(20, 20, 25, 0),
        XmlTime(17, 26, 1, 0),
        XmlTime(4, 7, 14, 0),
        XmlTime(16, 43, 46, 0),
        XmlTime(18, 17, 58, 0),
    )
    VALUE_20_36_58_21_24_31_20_49_32_03_41_03_20_16_36_21_16_33_09_49_53 = (
        XmlTime(20, 36, 58, 0),
        XmlTime(21, 24, 31, 0),
        XmlTime(20, 49, 32, 0),
        XmlTime(3, 41, 3, 0),
        XmlTime(20, 16, 36, 0),
        XmlTime(21, 16, 33, 0),
        XmlTime(9, 49, 53, 0),
    )
    VALUE_07_59_20_02_02_17_11_11_57_22_12_39_09_00_51_03_36_01_00_48_25_13_29_42 = (
        XmlTime(7, 59, 20, 0),
        XmlTime(2, 2, 17, 0),
        XmlTime(11, 11, 57, 0),
        XmlTime(22, 12, 39, 0),
        XmlTime(9, 0, 51, 0),
        XmlTime(3, 36, 1, 0),
        XmlTime(0, 48, 25, 0),
        XmlTime(13, 29, 42, 0),
    )
    VALUE_16_24_09_18_55_34_15_35_15_07_07_21_19_19_24_02_56_49_06_17_55_02_42_52 = (
        XmlTime(16, 24, 9, 0),
        XmlTime(18, 55, 34, 0),
        XmlTime(15, 35, 15, 0),
        XmlTime(7, 7, 21, 0),
        XmlTime(19, 19, 24, 0),
        XmlTime(2, 56, 49, 0),
        XmlTime(6, 17, 55, 0),
        XmlTime(2, 42, 52, 0),
    )
    VALUE_00_29_51_05_54_45_20_54_07_13_22_23_06_54_29_22_53_09_11_02_35_01_55_47 = (
        XmlTime(0, 29, 51, 0),
        XmlTime(5, 54, 45, 0),
        XmlTime(20, 54, 7, 0),
        XmlTime(13, 22, 23, 0),
        XmlTime(6, 54, 29, 0),
        XmlTime(22, 53, 9, 0),
        XmlTime(11, 2, 35, 0),
        XmlTime(1, 55, 47, 0),
    )
    VALUE_21_08_54_20_25_46_18_20_29_07_04_14_18_21_31_14_22_08_09_26_31 = (
        XmlTime(21, 8, 54, 0),
        XmlTime(20, 25, 46, 0),
        XmlTime(18, 20, 29, 0),
        XmlTime(7, 4, 14, 0),
        XmlTime(18, 21, 31, 0),
        XmlTime(14, 22, 8, 0),
        XmlTime(9, 26, 31, 0),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListTimeEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-time-enumeration-3-NS"

    value: NistschemaSvIvListTimeEnumeration3Type = field()
