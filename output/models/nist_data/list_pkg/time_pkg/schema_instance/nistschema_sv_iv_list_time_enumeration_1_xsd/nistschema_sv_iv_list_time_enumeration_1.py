from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-enumeration-1-NS"


class NistschemaSvIvListTimeEnumeration1Type(Enum):
    VALUE_16_22_20_01_19_11_21_37_24_12_13_13_14_56_46_19_02_14 = "16:22:20 01:19:11 21:37:24 12:13:13 14:56:46 19:02:14"
    VALUE_07_17_31_13_47_35_14_07_26_07_08_30_15_18_40_09_10_42 = "07:17:31 13:47:35 14:07:26 07:08:30 15:18:40 09:10:42"
    VALUE_18_10_11_22_21_23_23_58_22_17_08_12_08_14_52_00_17_12_03_05_44_20_23_12_19_52_22_06_09_32 = "18:10:11 22:21:23 23:58:22 17:08:12 08:14:52 00:17:12 03:05:44 20:23:12 19:52:22 06:09:32"
    VALUE_21_21_52_03_24_38_12_34_13_20_23_03_05_52_11_11_36_11_01_00_51 = "21:21:52 03:24:38 12:34:13 20:23:03 05:52:11 11:36:11 01:00:51"
    VALUE_17_14_09_06_52_14_10_05_58_17_05_37_22_36_07 = "17:14:09 06:52:14 10:05:58 17:05:37 22:36:07"
    VALUE_07_57_55_14_57_18_15_27_38_20_24_52_05_27_55 = "07:57:55 14:57:18 15:27:38 20:24:52 05:27:55"
    VALUE_02_50_34_03_25_09_15_41_25_13_28_11_12_21_19_05_03_58_08_08_30_01_14_08_18_54_43 = "02:50:34 03:25:09 15:41:25 13:28:11 12:21:19 05:03:58 08:08:30 01:14:08 18:54:43"


@dataclass
class NistschemaSvIvListTimeEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-time-enumeration-1-NS"

    value: Optional[NistschemaSvIvListTimeEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )