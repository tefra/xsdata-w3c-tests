from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-2-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlPeriod("--06-11"),
        },
    )
