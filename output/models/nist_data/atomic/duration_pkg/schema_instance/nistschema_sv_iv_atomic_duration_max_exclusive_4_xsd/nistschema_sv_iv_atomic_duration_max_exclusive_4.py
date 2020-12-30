from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-4-NS"

    value: Optional[Duration] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": Duration("P1983Y12M12DT16H37M58S"),
        }
    )
