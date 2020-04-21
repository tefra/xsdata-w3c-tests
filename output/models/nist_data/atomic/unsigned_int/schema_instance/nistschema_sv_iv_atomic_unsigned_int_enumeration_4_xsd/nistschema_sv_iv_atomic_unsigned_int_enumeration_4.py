from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-4-NS"


class NistschemaSvIvAtomicUnsignedIntEnumeration4Type(Enum):
    """
    :cvar VALUE_18558:
    :cvar VALUE_237992966:
    :cvar VALUE_271268:
    :cvar VALUE_47:
    :cvar VALUE_969778623:
    :cvar VALUE_9906:
    """
    VALUE_18558 = 18558
    VALUE_237992966 = 237992966
    VALUE_271268 = 271268
    VALUE_47 = 47
    VALUE_969778623 = 969778623
    VALUE_9906 = 9906


@dataclass
class NistschemaSvIvAtomicUnsignedIntEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedIntEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
