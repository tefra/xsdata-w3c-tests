from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-4-NS"


class NistschemaSvIvAtomicUnsignedIntEnumeration4Type(Enum):
    """
    :cvar VALUE_47:
    :cvar VALUE_9906:
    :cvar VALUE_271268:
    :cvar VALUE_18558:
    :cvar VALUE_969778623:
    :cvar VALUE_237992966:
    """
    VALUE_47 = 47
    VALUE_9906 = 9906
    VALUE_271268 = 271268
    VALUE_18558 = 18558
    VALUE_969778623 = 969778623
    VALUE_237992966 = 237992966


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
