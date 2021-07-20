from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-4-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "min_inclusive": XmlDate(1979, 3, 5),
        }
    )
