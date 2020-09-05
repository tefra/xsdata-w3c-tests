from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-3-NS"


class NistschemaSvIvAtomicGYearEnumeration3Type(Enum):
    """
    :cvar VALUE_2004:
    :cvar VALUE_2014:
    :cvar VALUE_1991:
    :cvar VALUE_2001:
    :cvar VALUE_2021:
    """
    VALUE_2004 = "2004"
    VALUE_2014 = "2014"
    VALUE_1991 = "1991"
    VALUE_2001 = "2001"
    VALUE_2021 = "2021"


@dataclass
class NistschemaSvIvAtomicGYearEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
