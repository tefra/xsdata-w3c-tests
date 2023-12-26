from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-1-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlDateTime(1970, 1, 1, 0, 0, 0),
        },
    )
