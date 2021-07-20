from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-3-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "max_exclusive": XmlPeriod("1971-05"),
        }
    )
