from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-5-NS"


class NistschemaSvIvAtomicUnsignedIntEnumeration5Type(Enum):
    """
    :cvar VALUE_34216:
    :cvar VALUE_276:
    :cvar VALUE_99184083:
    :cvar VALUE_7776:
    :cvar VALUE_6662698:
    :cvar VALUE_134172074:
    :cvar VALUE_93114:
    """
    VALUE_34216 = 34216
    VALUE_276 = 276
    VALUE_99184083 = 99184083
    VALUE_7776 = 7776
    VALUE_6662698 = 6662698
    VALUE_134172074 = 134172074
    VALUE_93114 = 93114


@dataclass
class NistschemaSvIvAtomicUnsignedIntEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedIntEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
