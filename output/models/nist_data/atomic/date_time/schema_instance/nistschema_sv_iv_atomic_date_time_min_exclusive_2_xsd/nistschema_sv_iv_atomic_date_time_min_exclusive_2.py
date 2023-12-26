from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlDateTime(1974, 4, 26, 23, 23, 51),
        },
    )
