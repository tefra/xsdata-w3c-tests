from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxInclusive-5-NS"

    value: Optional[Duration] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": Duration("P2030Y12M31DT23H59M59S"),
        }
    )
