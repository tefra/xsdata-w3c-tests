from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-enumeration-5-NS"


class NistschemaSvIvListTimeEnumeration5Type(Enum):
    VALUE_10_37_12_08_14_56_18_11_00_22_36_34_07_52_07_03_04_54_01_59_25_02_14_48_17_07_54 = "10:37:12 08:14:56 18:11:00 22:36:34 07:52:07 03:04:54 01:59:25 02:14:48 17:07:54"
    VALUE_23_02_41_07_44_16_06_05_22_13_27_20_23_25_59_06_39_31 = "23:02:41 07:44:16 06:05:22 13:27:20 23:25:59 06:39:31"
    VALUE_17_45_57_04_40_44_08_51_49_21_18_57_04_18_44_07_51_13_01_26_10_05_09_29_13_55_53 = "17:45:57 04:40:44 08:51:49 21:18:57 04:18:44 07:51:13 01:26:10 05:09:29 13:55:53"
    VALUE_07_33_34_20_36_44_17_18_46_13_11_44_21_04_49_17_55_06_06_14_06_11_00_54_01_46_48_19_42_04 = "07:33:34 20:36:44 17:18:46 13:11:44 21:04:49 17:55:06 06:14:06 11:00:54 01:46:48 19:42:04"
    VALUE_18_42_11_07_21_11_22_45_40_13_37_00_04_36_51_06_51_09_13_39_38_13_19_18_21_31_26 = "18:42:11 07:21:11 22:45:40 13:37:00 04:36:51 06:51:09 13:39:38 13:19:18 21:31:26"


@dataclass
class NistschemaSvIvListTimeEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-time-enumeration-5-NS"

    value: Optional[NistschemaSvIvListTimeEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )