from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-1-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlDateTime(1970, 1, 1, 0, 0, 0),
        },
    )
