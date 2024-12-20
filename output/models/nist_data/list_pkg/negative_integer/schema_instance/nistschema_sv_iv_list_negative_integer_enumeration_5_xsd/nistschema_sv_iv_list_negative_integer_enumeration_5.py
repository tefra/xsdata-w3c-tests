from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-negativeInteger-enumeration-5-NS"


class NistschemaSvIvListNegativeIntegerEnumeration5Type(Enum):
    VALUE_6243557272344_9413951478198_2712_19199_809130034748_78072 = (
        -6243557272344,
        -9413951478198,
        -2712,
        -19199,
        -809130034748,
        -78072,
    )
    VALUE_804609029232113_675_59472430230548822_724634598327_37641377388525987_3888278057058_8783960552_7401_100104 = (
        -804609029232113,
        -675,
        -59472430230548822,
        -724634598327,
        -37641377388525987,
        -3888278057058,
        -8783960552,
        -7401,
        -100104,
    )
    VALUE_54565175886_730_4886340658_88589090_12_6791121_8029718105_841978826501925 = (
        -54565175886,
        -730,
        -4886340658,
        -88589090,
        -12,
        -6791121,
        -8029718105,
        -841978826501925,
    )
    VALUE_833845019373395279_54025237462_7529_4_22_9299_4971413 = (
        -833845019373395279,
        -54025237462,
        -7529,
        -4,
        -22,
        -9299,
        -4971413,
    )
    VALUE_739989695435371_43059_62978526569606_954716417494343327_803490232286200201_447709680_1905_6873178 = (
        -739989695435371,
        -43059,
        -62978526569606,
        -954716417494343327,
        -803490232286200201,
        -447709680,
        -1905,
        -6873178,
    )
    VALUE_272_37538_4882800775886317_24112116788601_64438620666795132_53989_31753524240_7872667_5034281_683209724 = (
        -272,
        -37538,
        -4882800775886317,
        -24112116788601,
        -64438620666795132,
        -53989,
        -31753524240,
        -7872667,
        -5034281,
        -683209724,
    )
    VALUE_1544852_321_46754641_9545621_10641505851377_760307_125054610527_37568202029_75776 = (
        -1544852,
        -321,
        -46754641,
        -9545621,
        -10641505851377,
        -760307,
        -125054610527,
        -37568202029,
        -75776,
    )
    VALUE_68947924304193053_23770725041_5_1509302082020_22991649677_112802620330205_90 = (
        -68947924304193053,
        -23770725041,
        -5,
        -1509302082020,
        -22991649677,
        -112802620330205,
        -90,
    )
    VALUE_4330_24_19698544810949_170062967417_419_63_879002442589360_39 = (
        -4330,
        -24,
        -19698544810949,
        -170062967417,
        -419,
        -63,
        -879002442589360,
        -39,
    )


@dataclass
class NistschemaSvIvListNegativeIntegerEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-negativeInteger-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-negativeInteger-enumeration-5-NS"

    value: Optional[NistschemaSvIvListNegativeIntegerEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
