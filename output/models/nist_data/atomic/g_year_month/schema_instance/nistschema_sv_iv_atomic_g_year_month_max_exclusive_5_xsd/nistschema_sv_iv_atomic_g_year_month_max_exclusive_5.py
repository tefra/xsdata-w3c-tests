from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-5-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlPeriod("2030-12"),
        },
    )
