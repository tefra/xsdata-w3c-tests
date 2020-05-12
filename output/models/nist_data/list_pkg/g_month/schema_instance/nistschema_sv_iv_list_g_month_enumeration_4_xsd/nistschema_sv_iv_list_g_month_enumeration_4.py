from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-4-NS"


class NistschemaSvIvListGMonthEnumeration4Type(Enum):
    """
    :cvar VALUE_08_10_09_10_04_07_10_01_01:
    :cvar VALUE_03_06_11_09_02_08:
    :cvar VALUE_08_05_07_07_02_11_09:
    :cvar VALUE_06_08_04_09_06_10_09_01:
    :cvar VALUE_09_01_04_08_09_06_07_11_08:
    """
    VALUE_08_10_09_10_04_07_10_01_01 = "--08 --10 --09 --10 --04 --07 --10 --01 --01"
    VALUE_03_06_11_09_02_08 = "--03 --06 --11 --09 --02 --08"
    VALUE_08_05_07_07_02_11_09 = "--08 --05 --07 --07 --02 --11 --09"
    VALUE_06_08_04_09_06_10_09_01 = "--06 --08 --04 --09 --06 --10 --09 --01"
    VALUE_09_01_04_08_09_06_07_11_08 = "--09 --01 --04 --08 --09 --06 --07 --11 --08"


@dataclass
class NistschemaSvIvListGMonthEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-4-NS"

    value: Optional[NistschemaSvIvListGMonthEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
