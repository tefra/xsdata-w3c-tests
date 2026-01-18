from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-5-NS"


class NistschemaSvIvAtomicNameEnumeration5Type(Enum):
    TO_ENVIRONMENTS_DEFINE_IT_ISSUES_T = ":to.environments-define.it.issues.t"
    FI = ":fi"
    RAND_TO_AND_THE_C = "rand_to.and-the.c"
    THESE_KNOWN_QUALITY_APPLICATION_AVAILABLE_THE = (
        "_these-known.quality.application_available.the."
    )
    PAPPLICATION_THE_OBJECT_OBJECT_COMPUTING_CAN = (
        "papplication_the-object.object_computing_can"
    )
    DAND_APPLICA = "dand_applica"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNameEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-Name-enumeration-5-NS"

    value: NistschemaSvIvAtomicNameEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
