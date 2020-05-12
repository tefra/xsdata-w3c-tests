from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-5-NS"


class NistschemaSvIvAtomicNameEnumeration5Type(Enum):
    """
    :cvar DAND_APPLICA:
    :cvar FI:
    :cvar PAPPLICATION_THE_OBJECT_OBJECT_COMPUTING_CAN:
    :cvar RAND_TO_AND_THE_C:
    :cvar THESE_KNOWN_QUALITY_APPLICATION_AVAILABLE_THE:
    :cvar TO_ENVIRONMENTS_DEFINE_IT_ISSUES_T:
    """
    DAND_APPLICA = "dand_applica"
    FI = ":fi"
    PAPPLICATION_THE_OBJECT_OBJECT_COMPUTING_CAN = "papplication_the-object.object_computing_can"
    RAND_TO_AND_THE_C = "rand_to.and-the.c"
    THESE_KNOWN_QUALITY_APPLICATION_AVAILABLE_THE = "_these-known.quality.application_available.the."
    TO_ENVIRONMENTS_DEFINE_IT_ISSUES_T = ":to.environments-define.it.issues.t"


@dataclass
class NistschemaSvIvAtomicNameEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-Name-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicNameEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
