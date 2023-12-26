from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-4-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlPeriod("1970-06"),
        },
    )
