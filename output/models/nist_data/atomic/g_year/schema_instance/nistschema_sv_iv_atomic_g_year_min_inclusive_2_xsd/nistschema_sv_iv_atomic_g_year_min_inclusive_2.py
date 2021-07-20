from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGYearMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minInclusive-2-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "min_inclusive": XmlPeriod("2010"),
        }
    )
