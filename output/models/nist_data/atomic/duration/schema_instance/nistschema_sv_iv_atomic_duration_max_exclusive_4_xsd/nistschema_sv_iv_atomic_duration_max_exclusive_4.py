from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-4-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlDuration("P1983Y12M12DT16H37M58S"),
        }
    )
