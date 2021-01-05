from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-4-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlDateTime(2018, 6, 17, 15, 34, 43),
        }
    )
