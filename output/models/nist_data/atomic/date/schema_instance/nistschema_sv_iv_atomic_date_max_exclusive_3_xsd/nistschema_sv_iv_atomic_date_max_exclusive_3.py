from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-3-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlDate(1990, 1, 30),
        }
    )
