from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-enumeration-1-NS"


class NistschemaSvIvListFloatEnumeration1Type(Enum):
    VALUE_1_4_E_45_1_7368845_E_32_1_5052568_E_19_2_9911076_E_6_3_0409878_E7_2_0806022_E20_3_4028235_E38 = (
        "1.4E-45",
        "1.7368845E-32",
        "1.5052568E-19",
        "2.9911076E-6",
        "3.0409878E7",
        "2.0806022E20",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_3_2678537_E_29_2_3474718_E_13_2_2806252_E3_2_1494521_E19_3_4028235_E38 = (
        "1.4E-45",
        "3.2678537E-29",
        "2.3474718E-13",
        "2.2806252E3",
        "2.1494521E19",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_2_9988418_E_35_2_4667520_E_25_1_8664854_E_15_1_7673000_E_5_3_1331920_E5_2_6251418_E15_2_1423063_E25_3_4028235_E38 = (
        "1.4E-45",
        "2.9988418E-35",
        "2.4667520E-25",
        "1.8664854E-15",
        "1.7673000E-5",
        "3.1331920E5",
        "2.6251418E15",
        "2.1423063E25",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_1_7659206_E_34_3_2701442_E_23_1_6821211_E_12_2_2086680_E_1_1_6729408_E10_3_2413411_E21_3_4028235_E38 = (
        "1.4E-45",
        "1.7659206E-34",
        "3.2701442E-23",
        "1.6821211E-12",
        "2.2086680E-1",
        "1.6729408E10",
        "3.2413411E21",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_2_9465477_E_32_2_4841296_E_19_2_5718813_E_6_2_6682315_E7_2_7419164_E20_3_4028235_E38 = (
        "1.4E-45",
        "2.9465477E-32",
        "2.4841296E-19",
        "2.5718813E-6",
        "2.6682315E7",
        "2.7419164E20",
        "3.4028235E38",
    )
    VALUE_1_4_E_45_1_4381983_E_25_2_0448027_E_5_2_0920118_E15_3_4028235_E38 = (
        "1.4E-45",
        "1.4381983E-25",
        "2.0448027E-5",
        "2.0920118E15",
        "3.4028235E38",
    )


@dataclass
class NistschemaSvIvListFloatEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-float-enumeration-1-NS"

    value: Optional[NistschemaSvIvListFloatEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
