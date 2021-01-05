from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-1-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlDateTime(1970, 1, 1, 0, 0, 1),
        }
    )
