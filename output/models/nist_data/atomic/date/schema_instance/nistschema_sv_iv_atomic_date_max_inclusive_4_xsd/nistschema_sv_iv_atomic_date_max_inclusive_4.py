from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-date-maxInclusive-4-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlDate(1971, 1, 23),
        }
    )
