from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-5-NS"


class NistschemaSvIvAtomicDateEnumeration5Type(Enum):
    VALUE_1972_02_04 = "1972-02-04"
    VALUE_2010_06_24 = "2010-06-24"
    VALUE_2022_08_04 = "2022-08-04"
    VALUE_2006_12_31 = "2006-12-31"
    VALUE_1992_01_14 = "1992-01-14"
    VALUE_2027_09_16 = "2027-09-16"
    VALUE_1980_07_02 = "1980-07-02"
    VALUE_2013_06_03 = "2013-06-03"


@dataclass
class NistschemaSvIvAtomicDateEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicDateEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
