from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-enumeration-1-NS"


class NistschemaSvIvListStringEnumeration1Type(Enum):
    """
    :cvar AND_INFORMATION_THAT_REGISTRY_OF:
    :cvar A_BETTER_CHAIR_AND_OF_SPECIFICATIONS:
    :cvar BASIS_ANNUAL_FOR_CONDUCT_TO_FIRST_INCLUDING_THAT:
    :cvar COMPETENCE_FOR_AND_INTEROPERABILITY_RETRIEVAL_S:
    :cvar COMPLIANT_CONTAINING_XML_XSL_SERVICES:
    :cvar FILE_AND_AMBIGUITIES_HARDWARE_CONFERENCES_FOR:
    :cvar INTERNET_DEBUG_PERVASIVE_DISTRIBUTED_000_INTEROPERABILITY_AND_REFERENCE_PRINT:
    :cvar NIST_ITL_BUILDING_TRANSACTIONS_TO_IMPLEMENTATION_THE_SYSTEMS:
    :cvar OF_AND_ROLE_FACILITATION_APPLICATION_COMPUTED:
    :cvar THE_CONTAINING_BACK_PROVIDES_WIRELESS_TESTS_DOCUMENTS_BY_AS:
    """
    AND_INFORMATION_THAT_REGISTRY_OF = "and information that registry of"
    A_BETTER_CHAIR_AND_OF_SPECIFICATIONS = "a better chair and of specifications"
    BASIS_ANNUAL_FOR_CONDUCT_TO_FIRST_INCLUDING_THAT = "basis annual for Conduct to first including that"
    COMPETENCE_FOR_AND_INTEROPERABILITY_RETRIEVAL_S = "competence for and interoperability retrieval s"
    COMPLIANT_CONTAINING_XML_XSL_SERVICES = "compliant containing XML XSL services"
    FILE_AND_AMBIGUITIES_HARDWARE_CONFERENCES_FOR = "file and ambiguities hardware conferences for"
    INTERNET_DEBUG_PERVASIVE_DISTRIBUTED_000_INTEROPERABILITY_AND_REFERENCE_PRINT = "Internet debug pervasive distributed 000 interoperability and reference print"
    NIST_ITL_BUILDING_TRANSACTIONS_TO_IMPLEMENTATION_THE_SYSTEMS = "NIST/ITL building transactions to implementation the systems"
    OF_AND_ROLE_FACILITATION_APPLICATION_COMPUTED = "of and role Facilitation application computed"
    THE_CONTAINING_BACK_PROVIDES_WIRELESS_TESTS_DOCUMENTS_BY_AS = "the containing back provides wireless tests documents by as"


@dataclass
class NistschemaSvIvListStringEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-string-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-string-enumeration-1-NS"

    value: Optional[NistschemaSvIvListStringEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
