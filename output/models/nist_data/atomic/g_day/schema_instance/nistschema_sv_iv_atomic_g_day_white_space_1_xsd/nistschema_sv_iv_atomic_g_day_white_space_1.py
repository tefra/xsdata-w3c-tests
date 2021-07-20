from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicGDayWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-gDay-whiteSpace-1-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "white_space": "collapse",
        }
    )
