from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGDayMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gDay-minInclusive-4-NS"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlPeriod("---08"),
        },
    )
