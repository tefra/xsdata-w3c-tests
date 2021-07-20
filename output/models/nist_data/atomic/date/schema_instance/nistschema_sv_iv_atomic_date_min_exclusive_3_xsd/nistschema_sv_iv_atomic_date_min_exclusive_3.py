from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-3-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "min_exclusive": XmlDate(2005, 11, 17),
        }
    )
