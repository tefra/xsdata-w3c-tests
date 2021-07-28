from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-3-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDate(2005, 7, 30),
        }
    )
