from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-4-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlDuration("P2029Y10M29DT21H06M18S"),
        },
    )
