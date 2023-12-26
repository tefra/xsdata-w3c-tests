from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-4-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlPeriod("1981-02"),
        },
    )
