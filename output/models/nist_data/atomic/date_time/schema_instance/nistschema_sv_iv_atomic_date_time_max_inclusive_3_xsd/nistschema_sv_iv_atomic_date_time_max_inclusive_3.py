from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-3-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlDateTime(2003, 3, 9, 2, 0, 23),
        },
    )
