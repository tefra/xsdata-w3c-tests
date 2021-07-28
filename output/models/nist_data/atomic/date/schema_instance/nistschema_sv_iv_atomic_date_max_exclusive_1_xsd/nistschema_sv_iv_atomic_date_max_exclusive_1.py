from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-1-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlDate(1970, 1, 2),
        }
    )
