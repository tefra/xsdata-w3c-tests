from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicGYearMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-1-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlPeriod("1970"),
        },
    )
