from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-1-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDate(1970, 1, 1),
        }
    )
