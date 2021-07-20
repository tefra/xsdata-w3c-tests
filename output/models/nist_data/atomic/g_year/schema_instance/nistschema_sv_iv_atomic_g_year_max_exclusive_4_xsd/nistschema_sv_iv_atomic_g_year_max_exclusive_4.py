from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-4-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "max_exclusive": XmlPeriod("2005"),
        }
    )
