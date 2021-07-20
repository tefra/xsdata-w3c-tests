from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-5-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "max_exclusive": XmlDate(2030, 12, 31),
        }
    )
