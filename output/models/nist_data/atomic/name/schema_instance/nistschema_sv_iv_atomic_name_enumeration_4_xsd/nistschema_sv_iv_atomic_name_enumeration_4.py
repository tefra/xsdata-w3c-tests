from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-4-NS"


class NistschemaSvIvAtomicNameEnumeration4Type(Enum):
    """
    :cvar SPROVIDED_I:
    :cvar PRIGOROUS_MUST_THAN_S:
    :cvar JGENERATION_DEPLOYED_CONSISTENCY_VO:
    :cvar RSERVICES_AND_ELECTRONIC_TH:
    :cvar JFOR_ENABLING_AROUND_ELIMINATED_TO_FOR_BUSINESS_ORIENTED_I:
    :cvar OCAN_HAS_OF_TO_UNAMBI:
    :cvar MIS_AND_TO_HIGH_USE_CONFERENCE:
    """
    SPROVIDED_I = "sprovided:i"
    PRIGOROUS_MUST_THAN_S = "prigorous.must.than.s"
    JGENERATION_DEPLOYED_CONSISTENCY_VO = "jgeneration-deployed-consistency_vo"
    RSERVICES_AND_ELECTRONIC_TH = "rservices:and:electronic_th"
    JFOR_ENABLING_AROUND_ELIMINATED_TO_FOR_BUSINESS_ORIENTED_I = "jfor.enabling-around-eliminated-to.for-business-oriented_i"
    OCAN_HAS_OF_TO_UNAMBI = "ocan:has_of:to.unambi"
    MIS_AND_TO_HIGH_USE_CONFERENCE = "mis:and.to:high-use:conference"


@dataclass
class NistschemaSvIvAtomicNameEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-Name-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicNameEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
