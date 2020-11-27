from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-5-NS"


class NistschemaSvIvAtomicGYearEnumeration5Type(Enum):
    VALUE_2020 = "2020"
    VALUE_1988 = "1988"
    VALUE_1982 = "1982"
    VALUE_2000 = "2000"
    VALUE_1985 = "1985"
    VALUE_1994 = "1994"


@dataclass
class NistschemaSvIvAtomicGYearEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
