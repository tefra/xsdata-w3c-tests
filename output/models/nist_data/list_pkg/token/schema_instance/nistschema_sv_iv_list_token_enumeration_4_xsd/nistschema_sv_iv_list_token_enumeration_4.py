from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-enumeration-4-NS"


class NistschemaSvIvListTokenEnumeration4Type(Enum):
    MANUAL_ADOPTION_WHICH_SOFTWARE_TO_ONLY_XML_PC_INDUSTRY = "manual adoption which software to only XML PC industry"
    INDUSTRY_OF_BUILD_ACCESS_TO = "industry of build access to"
    FOR_TYPICAL_JOINT_YEARS_ONE = "for typical joint years One"
    OF_SECURITY_G_COMMERCE_FOR_BY_PERVASIVE_RETRIEVE_APPLICATIONS = "of security g commerce for by pervasive retrieve applications"
    COMPETENCE_FILE_IMPLEMENTATION_IS_NIST_ITL_WITH_ASSOCIATED = "competence file implementation is NIST/ITL with associated"
    PROFILES_IN_USED_OBJECTIVE_INVESTIGATION = "profiles in used objective investigation"
    OUTFITTING_MEET_COMPUTING_SECOND_GENERATION_LANGUAGE_USE_WITH = "outfitting meet computing second-generation Language use with"
    TRANSACTIONAL_OF_DEVELOPING_USING_THE = "transactional of developing using The"
    THAT_THE_TO_NETWORKING_TECHNOLOGIES = "that the to networking technologies"


@dataclass
class NistschemaSvIvListTokenEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-token-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-token-enumeration-4-NS"

    value: Optional[NistschemaSvIvListTokenEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
