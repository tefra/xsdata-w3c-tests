from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-4-NS"


class NistschemaSvIvAtomicNmtokenEnumeration4Type(Enum):
    """
    :cvar TRANS:
    :cvar OBJEC:
    :cvar MUST_INVESTIGATORS_SIGNATURES_TOOLS_SOFTWARE_TO_THAT_AS_RO:
    :cvar THAT_PROFILES_DEFI:
    :cvar RELATED_IMPLEMENTATION_SECURITY_CAPABILITIES_THAT:
    :cvar THE_OF_FILES_FOR_RECOMMENDATION_APPROPRIATE_DISCO:
    """
    TRANS = "trans"
    OBJEC = "Objec"
    MUST_INVESTIGATORS_SIGNATURES_TOOLS_SOFTWARE_TO_THAT_AS_RO = "must_Investigators_signatures:tools_software-to.that-as:ro"
    THAT_PROFILES_DEFI = "that_profiles:defi"
    RELATED_IMPLEMENTATION_SECURITY_CAPABILITIES_THAT = "related_implementation-security.capabilities:that"
    THE_OF_FILES_FOR_RECOMMENDATION_APPROPRIATE_DISCO = "The-of_files.for.Recommendation-appropriate-disco"


@dataclass
class NistschemaSvIvAtomicNmtokenEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicNmtokenEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
