from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-4-NS"


class NistschemaSvIvAtomicNameEnumeration4Type(Enum):
    SPROVIDED_I = "sprovided:i"
    PRIGOROUS_MUST_THAN_S = "prigorous.must.than.s"
    JGENERATION_DEPLOYED_CONSISTENCY_VO = "jgeneration-deployed-consistency_vo"
    RSERVICES_AND_ELECTRONIC_TH = "rservices:and:electronic_th"
    JFOR_ENABLING_AROUND_ELIMINATED_TO_FOR_BUSINESS_ORIENTED_I = (
        "jfor.enabling-around-eliminated-to.for-business-oriented_i"
    )
    OCAN_HAS_OF_TO_UNAMBI = "ocan:has_of:to.unambi"
    MIS_AND_TO_HIGH_USE_CONFERENCE = "mis:and.to:high-use:conference"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNameEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-Name-enumeration-4-NS"

    value: NistschemaSvIvAtomicNameEnumeration4Type = field()
