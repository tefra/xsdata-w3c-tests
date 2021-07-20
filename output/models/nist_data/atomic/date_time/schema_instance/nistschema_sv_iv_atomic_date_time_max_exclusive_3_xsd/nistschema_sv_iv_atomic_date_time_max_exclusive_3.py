from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-3-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "max_exclusive": XmlDateTime(1996, 8, 13, 0, 44, 39),
        }
    )
