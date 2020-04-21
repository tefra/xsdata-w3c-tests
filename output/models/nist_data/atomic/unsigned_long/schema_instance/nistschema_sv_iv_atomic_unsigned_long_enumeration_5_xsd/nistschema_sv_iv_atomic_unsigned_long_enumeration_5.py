from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-5-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration5Type(Enum):
    """
    :cvar VALUE_2880505374436178:
    :cvar VALUE_47:
    :cvar VALUE_62233091384207:
    :cvar VALUE_81098772:
    :cvar VALUE_858510565604495:
    :cvar VALUE_9211859:
    """
    VALUE_2880505374436178 = 2880505374436178
    VALUE_47 = 47
    VALUE_62233091384207 = 62233091384207
    VALUE_81098772 = 81098772
    VALUE_858510565604495 = 858510565604495
    VALUE_9211859 = 9211859


@dataclass
class NistschemaSvIvAtomicUnsignedLongEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedLongEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
