from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicGYearWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-gYear-whiteSpace-1-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
