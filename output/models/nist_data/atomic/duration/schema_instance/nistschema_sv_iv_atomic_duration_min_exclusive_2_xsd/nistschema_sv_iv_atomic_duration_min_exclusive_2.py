from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-2-NS"

    value: XmlDuration = field(
        metadata={
            "min_exclusive": XmlDuration("P2015Y06M12DT06H42M35S"),
        }
    )
