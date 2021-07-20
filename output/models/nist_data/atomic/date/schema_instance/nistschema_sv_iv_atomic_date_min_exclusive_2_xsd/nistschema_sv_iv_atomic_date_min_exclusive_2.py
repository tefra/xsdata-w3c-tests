from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-2-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "min_exclusive": XmlDate(2027, 3, 5),
        }
    )
