from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-5-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDateTime(2030, 12, 31, 23, 59, 59),
        },
    )
