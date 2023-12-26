from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-2-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDateTime(1972, 10, 10, 11, 7, 3),
        },
    )
