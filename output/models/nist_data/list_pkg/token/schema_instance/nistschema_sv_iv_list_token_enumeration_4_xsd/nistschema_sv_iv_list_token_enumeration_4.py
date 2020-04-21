from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-enumeration-4-NS"


class NistschemaSvIvListTokenEnumeration4Type(Enum):
    """
    :cvar COMPETENCE_FILE_IMPLEMENTATION_IS_NIST_ITL_WITH_ASSOCIATED:
    :cvar FOR_TYPICAL_JOINT_YEARS_ONE:
    :cvar INDUSTRY_OF_BUILD_ACCESS_TO:
    :cvar MANUAL_ADOPTION_WHICH_SOFTWARE_TO_ONLY_XML_PC_INDUSTRY:
    :cvar OF_SECURITY_G_COMMERCE_FOR_BY_PERVASIVE_RETRIEVE_APPLICATIONS:
    :cvar OUTFITTING_MEET_COMPUTING_SECOND_GENERATION_LANGUAGE_USE_WITH:
    :cvar PROFILES_IN_USED_OBJECTIVE_INVESTIGATION:
    :cvar THAT_THE_TO_NETWORKING_TECHNOLOGIES:
    :cvar TRANSACTIONAL_OF_DEVELOPING_USING_THE:
    """
    COMPETENCE_FILE_IMPLEMENTATION_IS_NIST_ITL_WITH_ASSOCIATED = "competence file implementation is NIST/ITL with associated"
    FOR_TYPICAL_JOINT_YEARS_ONE = "for typical joint years One"
    INDUSTRY_OF_BUILD_ACCESS_TO = "industry of build access to"
    MANUAL_ADOPTION_WHICH_SOFTWARE_TO_ONLY_XML_PC_INDUSTRY = "manual adoption which software to only XML PC industry"
    OF_SECURITY_G_COMMERCE_FOR_BY_PERVASIVE_RETRIEVE_APPLICATIONS = "of security g commerce for by pervasive retrieve applications"
    OUTFITTING_MEET_COMPUTING_SECOND_GENERATION_LANGUAGE_USE_WITH = "outfitting meet computing second-generation Language use with"
    PROFILES_IN_USED_OBJECTIVE_INVESTIGATION = "profiles in used objective investigation"
    THAT_THE_TO_NETWORKING_TECHNOLOGIES = "that the to networking technologies"
    TRANSACTIONAL_OF_DEVELOPING_USING_THE = "transactional of developing using The"


@dataclass
class NistschemaSvIvListTokenEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-token-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-token-enumeration-4-NS"

    value: Optional[NistschemaSvIvListTokenEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
