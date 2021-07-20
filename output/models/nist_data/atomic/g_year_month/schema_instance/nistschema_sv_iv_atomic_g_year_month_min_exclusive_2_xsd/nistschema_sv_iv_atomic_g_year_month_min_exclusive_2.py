from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-2-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "min_exclusive": XmlPeriod("2030-01"),
        }
    )
