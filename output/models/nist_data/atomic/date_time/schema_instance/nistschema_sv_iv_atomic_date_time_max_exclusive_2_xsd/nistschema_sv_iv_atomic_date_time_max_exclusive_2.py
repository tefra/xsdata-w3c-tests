from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-2-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "max_exclusive": XmlDateTime(1980, 5, 22, 13, 12, 9),
        }
    )
