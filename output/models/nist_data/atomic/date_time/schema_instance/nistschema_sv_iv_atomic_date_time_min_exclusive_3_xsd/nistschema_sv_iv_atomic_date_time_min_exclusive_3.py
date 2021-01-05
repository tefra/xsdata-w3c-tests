from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlDateTime(1981, 6, 8, 6, 29, 37),
        }
    )
