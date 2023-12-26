from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-1-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlDate(1970, 1, 1),
        },
    )
