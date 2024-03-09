from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxInclusive-4-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlDuration("P1989Y04M21DT11H28M41S"),
        },
    )
