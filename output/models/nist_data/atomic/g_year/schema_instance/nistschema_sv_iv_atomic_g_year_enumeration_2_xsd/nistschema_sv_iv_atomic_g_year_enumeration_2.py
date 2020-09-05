from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-2-NS"


class NistschemaSvIvAtomicGYearEnumeration2Type(Enum):
    """
    :cvar VALUE_2007:
    :cvar VALUE_2020:
    :cvar VALUE_1999:
    :cvar VALUE_2011:
    :cvar VALUE_1976:
    :cvar VALUE_1984:
    :cvar VALUE_1972:
    :cvar VALUE_1992:
    :cvar VALUE_2018:
    """
    VALUE_2007 = "2007"
    VALUE_2020 = "2020"
    VALUE_1999 = "1999"
    VALUE_2011 = "2011"
    VALUE_1976 = "1976"
    VALUE_1984 = "1984"
    VALUE_1972 = "1972"
    VALUE_1992 = "1992"
    VALUE_2018 = "2018"


@dataclass
class NistschemaSvIvAtomicGYearEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
