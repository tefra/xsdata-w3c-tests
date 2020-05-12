from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-4-NS"


class NistschemaSvIvAtomicStringEnumeration4Type(Enum):
    """
    :cvar EB_XML:
    :cvar MANY:
    :cvar THE:
    :cvar THE_1:
    :cvar VALUE_2000:
    """
    EB_XML = "ebXML"
    MANY = "many"
    THE = "the"
    THE_1 = "The"
    VALUE_2000 = "2000"


@dataclass
class NistschemaSvIvAtomicStringEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicStringEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
