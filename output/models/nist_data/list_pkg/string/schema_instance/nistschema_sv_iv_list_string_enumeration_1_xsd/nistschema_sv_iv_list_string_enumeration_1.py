from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-enumeration-1-NS"


class NistschemaSvIvListStringEnumeration1Type(Enum):
    OF_AND_ROLE_FACILITATION_APPLICATION_COMPUTED = (
            "of",
            "and",
            "role",
            "Facilitation",
            "application",
            "computed",
        )
    BASIS_ANNUAL_FOR_CONDUCT_TO_FIRST_INCLUDING_THAT = (
            "basis",
            "annual",
            "for",
            "Conduct",
            "to",
            "first",
            "including",
            "that",
        )
    THE_CONTAINING_BACK_PROVIDES_WIRELESS_TESTS_DOCUMENTS_BY_AS = (
            "the",
            "containing",
            "back",
            "provides",
            "wireless",
            "tests",
            "documents",
            "by",
            "as",
        )
    A_BETTER_CHAIR_AND_OF_SPECIFICATIONS = (
            "a",
            "better",
            "chair",
            "and",
            "of",
            "specifications",
        )
    COMPETENCE_FOR_AND_INTEROPERABILITY_RETRIEVAL_S = (
            "competence",
            "for",
            "and",
            "interoperability",
            "retrieval",
            "s",
        )
    COMPLIANT_CONTAINING_XML_XSL_SERVICES = (
            "compliant",
            "containing",
            "XML",
            "XSL",
            "services",
        )
    INTERNET_DEBUG_PERVASIVE_DISTRIBUTED_000_INTEROPERABILITY_AND_REFERENCE_PRINT = (
            "Internet",
            "debug",
            "pervasive",
            "distributed",
            "000",
            "interoperability",
            "and",
            "reference",
            "print",
        )
    FILE_AND_AMBIGUITIES_HARDWARE_CONFERENCES_FOR = (
            "file",
            "and",
            "ambiguities",
            "hardware",
            "conferences",
            "for",
        )
    NIST_ITL_BUILDING_TRANSACTIONS_TO_IMPLEMENTATION_THE_SYSTEMS = (
            "NIST/ITL",
            "building",
            "transactions",
            "to",
            "implementation",
            "the",
            "systems",
        )
    AND_INFORMATION_THAT_REGISTRY_OF = (
            "and",
            "information",
            "that",
            "registry",
            "of",
        )


@dataclass
class NistschemaSvIvListStringEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-string-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-string-enumeration-1-NS"

    value: Optional[NistschemaSvIvListStringEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
