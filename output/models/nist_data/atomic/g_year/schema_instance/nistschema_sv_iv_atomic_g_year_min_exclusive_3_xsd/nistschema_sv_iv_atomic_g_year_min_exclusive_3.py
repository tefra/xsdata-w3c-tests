from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicGYearMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minExclusive-3-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "min_exclusive": XmlPeriod("2025"),
        }
    )
