from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-enumeration-5-NS"


class NistschemaSvIvListUnsignedIntEnumeration5Type(Enum):
    VALUE_4790_705422250_494_4294967295_6118_71_490_980151_763670898_578 = (
        4790,
        705422250,
        494,
        4294967295,
        6118,
        71,
        490,
        980151,
        763670898,
        578,
    )
    VALUE_320_12338_202_8802187_95929_91652152_40482 = (
        320,
        12338,
        202,
        8802187,
        95929,
        91652152,
        40482,
    )
    VALUE_34756_159_515837953_46288_31 = (
        34756,
        159,
        515837953,
        46288,
        31,
    )
    VALUE_5_163803_84_43983_3102378450 = (
        5,
        163803,
        84,
        43983,
        3102378450,
    )
    VALUE_78_9714250_39_31_1575032_875293721_301345_3955_823756 = (
        78,
        9714250,
        39,
        31,
        1575032,
        875293721,
        301345,
        3955,
        823756,
    )
    VALUE_3_558_49_10715829_68_508503_4294967295_7301916 = (
        3,
        558,
        49,
        10715829,
        68,
        508503,
        4294967295,
        7301916,
    )
    VALUE_1369750_135_28_91_3571_223722983_940805014_452629 = (
        1369750,
        135,
        28,
        91,
        3571,
        223722983,
        940805014,
        452629,
    )
    VALUE_44425889_209188253_174559_698388_35_3158276_105 = (
        44425889,
        209188253,
        174559,
        698388,
        35,
        3158276,
        105,
    )
    VALUE_60_257_82546925_5499636_9029392_909675_267687_7391_21 = (
        60,
        257,
        82546925,
        5499636,
        9029392,
        909675,
        267687,
        7391,
        21,
    )


@dataclass
class NistschemaSvIvListUnsignedIntEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-enumeration-5-NS"

    value: Optional[NistschemaSvIvListUnsignedIntEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
