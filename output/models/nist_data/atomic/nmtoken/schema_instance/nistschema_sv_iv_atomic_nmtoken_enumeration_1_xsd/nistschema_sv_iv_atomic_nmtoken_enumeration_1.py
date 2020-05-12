from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-1-NS"


class NistschemaSvIvAtomicNmtokenEnumeration1Type(Enum):
    """
    :cvar COLLABORATE_TOOLS_WE_WITH_EACH_THE_RELATIONSHIPS_NETWOR:
    :cvar COMPUTING_NSRL_CAN_A_TO_OF_MUST_PERV:
    :cvar INTERNET_WILL_THAT_TO_MAD:
    :cvar LAUNCHING_CORRECTNESS_REVISIONS_AND_SP:
    :cvar THAT_COST_BUSINESS_FOR_ARE_INDUSTRIES_PROCESSES_PICO:
    """
    COLLABORATE_TOOLS_WE_WITH_EACH_THE_RELATIONSHIPS_NETWOR = "collaborate-tools-we_with.each.the_relationships_networ"
    COMPUTING_NSRL_CAN_A_TO_OF_MUST_PERV = "computing-NSRL.can:a.to-of:must-perv"
    INTERNET_WILL_THAT_TO_MAD = "Internet_will:_that:to_mad"
    LAUNCHING_CORRECTNESS_REVISIONS_AND_SP = "launching.correctness_revisions_and.sp"
    THAT_COST_BUSINESS_FOR_ARE_INDUSTRIES_PROCESSES_PICO = "that.cost_Business-for_are:industries:processes_pico-"


@dataclass
class NistschemaSvIvAtomicNmtokenEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicNmtokenEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
