from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxInclusive-2-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlDuration("P1970Y02M12DT08H03M16S"),
        },
    )
