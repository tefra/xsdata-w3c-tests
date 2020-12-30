from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicDurationWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-whiteSpace-1-NS"

    value: Optional[Duration] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
