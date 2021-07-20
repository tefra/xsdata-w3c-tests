from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonPositiveInteger-enumeration-3-NS"


class NistschemaSvIvListNonPositiveIntegerEnumeration3Type(Enum):
    VALUE_129861294408_1667568262_41487869_7875363_32 = (
            -129861294408,
            -1667568262,
            -41487869,
            -7875363,
            -32,
        )
    VALUE_20654933970_19615378145173_1076661839237_20837398_401663551838 = (
            -20654933970,
            -19615378145173,
            -1076661839237,
            -20837398,
            -401663551838,
        )
    VALUE_394_2137_35774872303308891_456801256964287_3415_354007 = (
            -394,
            -2137,
            -35774872303308891,
            -456801256964287,
            -3415,
            -354007,
        )
    VALUE_46300627_8_8076536_216167698040_969_101910654786010_4010810_994 = (
            -46300627,
            -8,
            -8076536,
            -216167698040,
            -969,
            -101910654786010,
            -4010810,
            -994,
        )
    VALUE_28315387_8631_252432056684130_215190945_654652471771561_88_75753184355300 = (
            -28315387,
            -8631,
            -252432056684130,
            -215190945,
            -654652471771561,
            -88,
            -75753184355300,
        )
    VALUE_501942814_169879871_393_56515288629263_46857283_682224_1682_2142906705356_1702765287_447641597 = (
            -501942814,
            -169879871,
            -393,
            -56515288629263,
            -46857283,
            -682224,
            -1682,
            -2142906705356,
            -1702765287,
            -447641597,
        )


@dataclass
class NistschemaSvIvListNonPositiveIntegerEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonPositiveInteger-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-nonPositiveInteger-enumeration-3-NS"

    value: Optional[NistschemaSvIvListNonPositiveIntegerEnumeration3Type] = field(
        default=None
    )
