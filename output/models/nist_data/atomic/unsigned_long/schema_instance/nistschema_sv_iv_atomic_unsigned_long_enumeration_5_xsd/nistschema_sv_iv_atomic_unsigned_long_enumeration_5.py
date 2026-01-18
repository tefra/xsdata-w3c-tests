from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-5-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration5Type(Enum):
    VALUE_47 = 47
    VALUE_62233091384207 = 62233091384207
    VALUE_9211859 = 9211859
    VALUE_81098772 = 81098772
    VALUE_2880505374436178 = 2880505374436178
    VALUE_858510565604495 = 858510565604495


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedLongEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-5-NS"

    value: NistschemaSvIvAtomicUnsignedLongEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
