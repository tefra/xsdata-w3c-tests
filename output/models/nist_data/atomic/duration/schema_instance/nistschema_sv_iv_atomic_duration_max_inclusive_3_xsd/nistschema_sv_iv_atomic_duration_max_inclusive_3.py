from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxInclusive-3-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlDuration("P1981Y03M20DT22H33M14S"),
        },
    )
