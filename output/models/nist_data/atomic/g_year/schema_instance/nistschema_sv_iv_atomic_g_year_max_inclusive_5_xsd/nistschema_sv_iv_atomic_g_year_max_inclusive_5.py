from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-5-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "max_inclusive": XmlPeriod("2030"),
        }
    )
