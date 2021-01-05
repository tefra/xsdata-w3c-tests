from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-4-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlDate(2025, 1, 9),
        }
    )
