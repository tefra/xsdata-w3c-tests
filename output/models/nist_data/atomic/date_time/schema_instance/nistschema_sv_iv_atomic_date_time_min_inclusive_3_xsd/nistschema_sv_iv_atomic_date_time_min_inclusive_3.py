from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDateTime(1978, 11, 30, 10, 14, 33),
        },
    )
