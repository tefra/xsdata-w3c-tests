from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-2-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlDuration("P1990Y06M11DT15H00M05S"),
        },
    )
