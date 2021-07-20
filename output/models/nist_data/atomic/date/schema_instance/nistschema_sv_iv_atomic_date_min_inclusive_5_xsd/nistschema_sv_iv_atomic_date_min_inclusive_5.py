from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDateMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-5-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "min_inclusive": XmlDate(2030, 12, 31),
        }
    )
