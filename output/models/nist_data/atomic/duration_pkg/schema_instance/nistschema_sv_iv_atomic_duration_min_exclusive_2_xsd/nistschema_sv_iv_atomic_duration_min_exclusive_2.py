from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-2-NS"

    value: Optional[Duration] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Duration("P2015Y06M12DT06H42M35S"),
        }
    )
