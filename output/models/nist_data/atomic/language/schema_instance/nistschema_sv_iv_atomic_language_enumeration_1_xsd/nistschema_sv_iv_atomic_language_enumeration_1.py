from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-enumeration-1-NS"


class NistschemaSvIvAtomicLanguageEnumeration1Type(Enum):
    """
    :cvar AF:
    :cvar AM:
    :cvar AR:
    :cvar AS_VALUE:
    :cvar AY:
    :cvar AZ:
    :cvar BA:
    :cvar BE:
    """
    AF = "AF"
    AM = "AM"
    AR = "AR"
    AS_VALUE = "AS"
    AY = "AY"
    AZ = "AZ"
    BA = "BA"
    BE = "BE"


@dataclass
class NistschemaSvIvAtomicLanguageEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicLanguageEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
