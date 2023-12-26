from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-5-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlPeriod("2030-12"),
        },
    )
