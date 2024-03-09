from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-enumeration-5-NS"


class NistschemaSvIvListTimeEnumeration5Type(Enum):
    VALUE_10_37_12_08_14_56_18_11_00_22_36_34_07_52_07_03_04_54_01_59_25_02_14_48_17_07_54 = (
        XmlTime(10, 37, 12, 0),
        XmlTime(8, 14, 56, 0),
        XmlTime(18, 11, 0, 0),
        XmlTime(22, 36, 34, 0),
        XmlTime(7, 52, 7, 0),
        XmlTime(3, 4, 54, 0),
        XmlTime(1, 59, 25, 0),
        XmlTime(2, 14, 48, 0),
        XmlTime(17, 7, 54, 0),
    )
    VALUE_23_02_41_07_44_16_06_05_22_13_27_20_23_25_59_06_39_31 = (
        XmlTime(23, 2, 41, 0),
        XmlTime(7, 44, 16, 0),
        XmlTime(6, 5, 22, 0),
        XmlTime(13, 27, 20, 0),
        XmlTime(23, 25, 59, 0),
        XmlTime(6, 39, 31, 0),
    )
    VALUE_17_45_57_04_40_44_08_51_49_21_18_57_04_18_44_07_51_13_01_26_10_05_09_29_13_55_53 = (
        XmlTime(17, 45, 57, 0),
        XmlTime(4, 40, 44, 0),
        XmlTime(8, 51, 49, 0),
        XmlTime(21, 18, 57, 0),
        XmlTime(4, 18, 44, 0),
        XmlTime(7, 51, 13, 0),
        XmlTime(1, 26, 10, 0),
        XmlTime(5, 9, 29, 0),
        XmlTime(13, 55, 53, 0),
    )
    VALUE_07_33_34_20_36_44_17_18_46_13_11_44_21_04_49_17_55_06_06_14_06_11_00_54_01_46_48_19_42_04 = (
        XmlTime(7, 33, 34, 0),
        XmlTime(20, 36, 44, 0),
        XmlTime(17, 18, 46, 0),
        XmlTime(13, 11, 44, 0),
        XmlTime(21, 4, 49, 0),
        XmlTime(17, 55, 6, 0),
        XmlTime(6, 14, 6, 0),
        XmlTime(11, 0, 54, 0),
        XmlTime(1, 46, 48, 0),
        XmlTime(19, 42, 4, 0),
    )
    VALUE_18_42_11_07_21_11_22_45_40_13_37_00_04_36_51_06_51_09_13_39_38_13_19_18_21_31_26 = (
        XmlTime(18, 42, 11, 0),
        XmlTime(7, 21, 11, 0),
        XmlTime(22, 45, 40, 0),
        XmlTime(13, 37, 0, 0),
        XmlTime(4, 36, 51, 0),
        XmlTime(6, 51, 9, 0),
        XmlTime(13, 39, 38, 0),
        XmlTime(13, 19, 18, 0),
        XmlTime(21, 31, 26, 0),
    )


@dataclass
class NistschemaSvIvListTimeEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-time-enumeration-5-NS"

    value: Optional[NistschemaSvIvListTimeEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
