from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlPeriod("2030-11"),
        },
    )
