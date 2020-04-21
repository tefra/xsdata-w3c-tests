from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-4-NS"


class NistschemaSvIvAtomicGYearEnumeration4Type(Enum):
    """
    :cvar VALUE_1970:
    :cvar VALUE_1978:
    :cvar VALUE_2002:
    :cvar VALUE_2007:
    :cvar VALUE_2014:
    :cvar VALUE_2015:
    :cvar VALUE_2016:
    :cvar VALUE_2021:
    :cvar VALUE_2023:
    :cvar VALUE_2027:
    """
    VALUE_1970 = "1970"
    VALUE_1978 = "1978"
    VALUE_2002 = "2002"
    VALUE_2007 = "2007"
    VALUE_2014 = "2014"
    VALUE_2015 = "2015"
    VALUE_2016 = "2016"
    VALUE_2021 = "2021"
    VALUE_2023 = "2023"
    VALUE_2027 = "2027"


@dataclass
class NistschemaSvIvAtomicGYearEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
