from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-5-NS"


class NistschemaSvIvAtomicNmtokenEnumeration5Type(Enum):
    """
    :cvar CROSS_OVER_RELATED_AMBIGUITIES_THE_EX:
    :cvar DEFINE_A_SCHEMAS_OASIS_WORKING_CONFERENCE_PROFI:
    :cvar HAVE_AUTOMATIC:
    :cvar OBJECT_RAPID_OF_PARTNERS_INCLUDING_DOCUME:
    :cvar ONLY_D:
    :cvar PROMINENT_RETRIEVE_RIGOROUS_A_OF_FOR_DEFINE_AND_PARTICIPANTS_JA:
    :cvar VIA_DISCUSSIONS:
    """
    CROSS_OVER_RELATED_AMBIGUITIES_THE_EX = "cross-over.related.ambiguities-The.Ex"
    DEFINE_A_SCHEMAS_OASIS_WORKING_CONFERENCE_PROFI = "define.a:Schemas-OASIS:working.Conference_profi"
    HAVE_AUTOMATIC = "have_automatic"
    OBJECT_RAPID_OF_PARTNERS_INCLUDING_DOCUME = "object_rapid.of:partners:including.docume"
    ONLY_D = "only:d"
    PROMINENT_RETRIEVE_RIGOROUS_A_OF_FOR_DEFINE_AND_PARTICIPANTS_JA = "prominent_retrieve_rigorous.a:of-for.define-and:participants:Ja"
    VIA_DISCUSSIONS = "via.discussions"


@dataclass
class NistschemaSvIvAtomicNmtokenEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicNmtokenEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
