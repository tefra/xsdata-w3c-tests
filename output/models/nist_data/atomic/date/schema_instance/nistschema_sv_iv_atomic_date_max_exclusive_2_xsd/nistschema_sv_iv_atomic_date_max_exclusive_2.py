from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-2-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlDate(2016, 9, 5),
        },
    )
