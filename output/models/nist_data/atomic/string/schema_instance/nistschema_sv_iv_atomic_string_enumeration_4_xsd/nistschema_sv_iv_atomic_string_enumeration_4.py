from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-4-NS"


class NistschemaSvIvAtomicStringEnumeration4Type(Enum):
    """
    :cvar THE:
    :cvar EB_XML:
    :cvar THE_1:
    :cvar MANY:
    :cvar VALUE_2000:
    """
    THE = "the"
    EB_XML = "ebXML"
    THE_1 = "The"
    MANY = "many"
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
