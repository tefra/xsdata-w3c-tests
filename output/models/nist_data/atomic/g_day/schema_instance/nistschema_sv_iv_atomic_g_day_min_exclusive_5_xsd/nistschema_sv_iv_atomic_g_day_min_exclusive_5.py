from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-minExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGDayMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gDay-minExclusive-5-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "min_exclusive": XmlPeriod("---30"),
        }
    )
