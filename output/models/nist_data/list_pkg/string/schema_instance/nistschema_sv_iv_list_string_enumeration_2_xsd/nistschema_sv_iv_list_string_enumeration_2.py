from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-enumeration-2-NS"


class NistschemaSvIvListStringEnumeration2Type(Enum):
    PROFILE_RELATED_PROJECTOR_THE_INFORMATION_COMPATIBILITY_SOFTWARE_PROJECT = (
        "profile",
        "related",
        "projector",
        "the",
        "Information",
        "compatibility",
        "software",
        "Project",
    )
    THIS_APPROPRIATE_DUE_NIST_ITL_COMMUNICATION_DEFINE = (
        "this",
        "appropriate",
        "due",
        "NIST/ITL",
        "communication",
        "define",
    )
    UTILIZE_EC_TO_AS_XSL_FO_XML_ENSURE = (
        "utilize",
        "EC",
        "to",
        "as",
        "XSL-FO",
        "XML",
        "ensure",
    )
    PORTABLE_FIRST_GENERATION_NEED_MARKET_THE_PROVIDES = (
        "portable",
        "first-generation",
        "need",
        "market",
        "The",
        "provides",
    )
    AN_THE_BE_TOOLS_FILES_THAT = (
        "An",
        "the",
        "be",
        "tools",
        "files",
        "that",
    )
    ON_THAT_NETWORKS_LACK_TO_THE = (
        "on",
        "that",
        "networks",
        "lack",
        "to",
        "the",
    )
    ADVANCEMENT_DEFINING_MANY_STRUCTURED_S_AROUND_EMBEDDED = (
        "Advancement",
        "defining",
        "many",
        "Structured",
        "s",
        "around",
        "embedded",
    )
    TESTS_THE_DOCUMENTS_COMPLEX_THE_THESE = (
        "tests",
        "The",
        "documents",
        "complex",
        "the",
        "these",
    )
    INCLUDING_A_AND_PROCESS_XML_RELATED_PROJECT_SPECIFICATIONS_PICO_CELLULAR_THEREFORE_AS = (
        "including",
        "a",
        "and",
        "process",
        "XML-related",
        "project",
        "specifications",
        "pico-cellular",
        "Therefore",
        "as",
    )


@dataclass
class NistschemaSvIvListStringEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-string-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-string-enumeration-2-NS"

    value: Optional[NistschemaSvIvListStringEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
