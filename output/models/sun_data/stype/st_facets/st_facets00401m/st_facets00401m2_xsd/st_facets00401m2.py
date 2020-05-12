from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_00:
    :cvar VALUE_0:
    :cvar A0:
    :cvar VALUE_01:
    :cvar VALUE_1:
    :cvar A1:
    :cvar VALUE_02:
    :cvar VALUE_2:
    :cvar A2:
    :cvar VALUE_03:
    :cvar VALUE_3:
    :cvar A3:
    :cvar VALUE_04:
    :cvar VALUE_4:
    :cvar A4:
    :cvar VALUE_05:
    :cvar VALUE_5:
    :cvar A5:
    :cvar VALUE_06:
    :cvar VALUE_6:
    :cvar A6:
    :cvar VALUE_07:
    :cvar VALUE_7:
    :cvar A7:
    :cvar VALUE_08:
    :cvar VALUE_8:
    :cvar A8:
    :cvar VALUE_09:
    :cvar VALUE_9:
    :cvar A9:
    """
    VALUE_00 = "Ŋ00"
    VALUE_0 = "Ť-0"
    A0 = "ža0"
    VALUE_01 = "ƀ01"
    VALUE_1 = "Ɗ-1"
    A1 = "Ɣa1"
    VALUE_02 = "Ɩ02"
    VALUE_2 = "Ɲ-2"
    A2 = "ƥa2"
    VALUE_03 = "Ƨ03"
    VALUE_3 = "ƨ-3"
    A3 = "Ʃa3"
    VALUE_04 = "ƫ04"
    VALUE_4 = "ƴ-4"
    A4 = "ƽa4"
    VALUE_05 = "ǀ05"
    VALUE_5 = "ǁ-5"
    A5 = "ǃa5"
    VALUE_06 = "Ǎ06"
    VALUE_6 = "Ǟ-6"
    A6 = "ǯa6"
    VALUE_07 = "Ǵ07"
    VALUE_7 = "Ǵ-7"
    A7 = "ǵa7"
    VALUE_08 = "Ǻ08"
    VALUE_8 = "Ȉ-8"
    A8 = "ȗa8"
    VALUE_09 = "ɐ09"
    VALUE_9 = "ɢ-9"
    A9 = "ɴa9"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: List[S] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
