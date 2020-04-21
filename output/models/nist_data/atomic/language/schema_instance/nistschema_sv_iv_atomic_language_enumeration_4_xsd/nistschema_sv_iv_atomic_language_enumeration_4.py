from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-enumeration-4-NS"


class NistschemaSvIvAtomicLanguageEnumeration4Type(Enum):
    """
    :cvar BR:
    :cvar CA:
    :cvar CO:
    :cvar CS:
    :cvar CY:
    """
    BR = "BR"
    CA = "CA"
    CO = "CO"
    CS = "CS"
    CY = "CY"


@dataclass
class NistschemaSvIvAtomicLanguageEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicLanguageEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
