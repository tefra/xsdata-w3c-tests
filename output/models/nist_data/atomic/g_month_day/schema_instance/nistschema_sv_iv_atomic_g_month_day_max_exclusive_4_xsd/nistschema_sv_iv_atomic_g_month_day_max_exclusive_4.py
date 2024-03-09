from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-maxExclusive-4-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlPeriod("--11-27"),
        },
    )
