from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-4-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlDate(2027, 10, 13),
        },
    )
