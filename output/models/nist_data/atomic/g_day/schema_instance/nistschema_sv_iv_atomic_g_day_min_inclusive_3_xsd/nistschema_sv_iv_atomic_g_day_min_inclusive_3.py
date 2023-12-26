from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicGDayMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gDay-minInclusive-3-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlPeriod("---24"),
        },
    )
