from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-enumeration-3-NS"


class NistschemaSvIvListFloatEnumeration3Type(Enum):
    VALUE_1_4_E_45_2_9627340_E_32_2_9339876_E_19_1_6214040_E_6_3_2003688_E7_3_2639795_E20_3_4028235_E38 = (
        "1.4E-45",
        "2.9627340E-32",
        "2.9339876E-19",
        "1.6214040E-6",
        "3.2003688E7",
        "3.2639795E20",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_2_0448991_E_36_2_5812244_E_27_1_8634631_E_18_1_8560691_E_9_1_5748861_E0_1_5982703_E9_1_7326648_E18_2_1598972_E27_3_4028235_E38 = (
        "1.4E-45",
        "2.0448991E-36",
        "2.5812244E-27",
        "1.8634631E-18",
        "1.8560691E-9",
        "1.5748861E0",
        "1.5982703E9",
        "1.7326648E18",
        "2.1598972E27",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_2_6849324_E_25_2_2248837_E_5_3_1060941_E15_3_4028235_E38 = (
        "1.4E-45",
        "2.6849324E-25",
        "2.2248837E-5",
        "3.1060941E15",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_3_1420954_E_32_3_3769693_E_19_2_9315644_E_6_2_4746801_E7_2_8636274_E20_3_4028235_E38 = (
        "1.4E-45",
        "3.1420954E-32",
        "3.3769693E-19",
        "2.9315644E-6",
        "2.4746801E7",
        "2.8636274E20",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_2_9393671_E_32_2_6364556_E_19_2_8349156_E_6_2_1858090_E7_2_1197131_E20_3_4028235_E38 = (
        "1.4E-45",
        "2.9393671E-32",
        "2.6364556E-19",
        "2.8349156E-6",
        "2.1858090E7",
        "2.1197131E20",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_2_8634233_E_29_1_8700098_E_13_3_3100354_E3_1_4520848_E19_3_4028235_E38 = (
        "1.4E-45",
        "2.8634233E-29",
        "1.8700098E-13",
        "3.3100354E3",
        "1.4520848E19",
        "3.4028235E38",
    )


@dataclass
class NistschemaSvIvListFloatEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-float-enumeration-3-NS"

    value: Optional[NistschemaSvIvListFloatEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
