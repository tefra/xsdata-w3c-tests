from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDateTime(2006, 7, 21, 1, 32, 21),
        },
    )
