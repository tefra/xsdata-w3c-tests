from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-enumeration-4-NS"


class NistschemaSvIvListTimeEnumeration4Type(Enum):
    VALUE_20_55_32_13_12_24_05_09_54_15_26_04_21_18_52_07_04_22_13_43_48 = "20:55:32 13:12:24 05:09:54 15:26:04 21:18:52 07:04:22 13:43:48"
    VALUE_21_26_26_11_23_05_22_27_57_02_41_13_12_19_00_18_13_44 = "21:26:26 11:23:05 22:27:57 02:41:13 12:19:00 18:13:44"
    VALUE_07_27_57_09_04_49_17_05_01_12_15_48_01_00_58_10_04_48 = "07:27:57 09:04:49 17:05:01 12:15:48 01:00:58 10:04:48"
    VALUE_23_21_47_07_35_16_02_59_18_22_55_26_02_20_03 = "23:21:47 07:35:16 02:59:18 22:55:26 02:20:03"
    VALUE_08_08_33_21_55_09_10_27_06_14_09_32_22_18_18_11_48_00_11_07_55_14_18_46_16_46_53_14_53_55 = "08:08:33 21:55:09 10:27:06 14:09:32 22:18:18 11:48:00 11:07:55 14:18:46 16:46:53 14:53:55"
    VALUE_23_33_25_12_19_16_03_56_40_07_24_55_21_32_06_11_28_14_20_10_08_14_11_43 = "23:33:25 12:19:16 03:56:40 07:24:55 21:32:06 11:28:14 20:10:08 14:11:43"
    VALUE_09_02_38_04_10_17_21_01_45_10_23_34_07_06_37_06_19_51_06_20_06_19_54_42_12_23_53 = "09:02:38 04:10:17 21:01:45 10:23:34 07:06:37 06:19:51 06:20:06 19:54:42 12:23:53"
    VALUE_14_33_48_01_19_39_07_15_06_05_12_11_21_08_03_03_02_34_04_16_29_09_27_29_19_36_04_09_00_20 = "14:33:48 01:19:39 07:15:06 05:12:11 21:08:03 03:02:34 04:16:29 09:27:29 19:36:04 09:00:20"
    VALUE_04_52_05_18_26_53_04_51_11_01_39_09_16_03_11_15_17_05_03_31_28_14_31_06 = "04:52:05 18:26:53 04:51:11 01:39:09 16:03:11 15:17:05 03:31:28 14:31:06"
    VALUE_10_19_34_00_35_24_17_00_23_17_00_38_16_54_19_19_35_48_15_15_24_00_09_08_16_23_31 = "10:19:34 00:35:24 17:00:23 17:00:38 16:54:19 19:35:48 15:15:24 00:09:08 16:23:31"


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