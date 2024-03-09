from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-maxInclusive-2-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlDate(2029, 9, 9),
        },
    )
