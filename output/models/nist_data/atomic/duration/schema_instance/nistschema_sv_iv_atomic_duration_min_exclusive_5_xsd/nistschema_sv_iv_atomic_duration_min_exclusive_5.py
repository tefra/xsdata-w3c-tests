from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-5-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlDuration("P2030Y12M31DT23H59M58S"),
        },
    )
