from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-enumeration-4-NS"


class NistschemaSvIvListStringEnumeration4Type(Enum):
    MANIPULATE_IS_THIS_OF_WOULD_BUILT_FOR_USE = (
            "manipulate",
            "is",
            "this",
            "of",
            "would",
            "built",
            "for",
            "use",
        )
    AND_DEVELOPING_OBJECT_NSRL_MAINTAINED_MEETS_THE_IMPLEMENTATIONS_MANIPULATE = (
            "and",
            "developing",
            "object",
            "NSRL",
            "maintained",
            "meets",
            "the",
            "implementations",
            "manipulate",
        )
    A_THE_SUPPLY_THE_AND_POPULAR_UNBIASED = (
            "a",
            "The",
            "supply",
            "the",
            "and",
            "popular",
            "unbiased",
        )
    INVESTIGATION_TO_THE_CAPABILITIES_THEM = (
            "investigation",
            "to",
            "the",
            "capabilities",
            "them",
        )
    ORGANIZATIONS_SCREEN_SUBCOMMITTEE_STANDARDS_SIMULATION_METHODS = (
            "organizations",
            "screen",
            "Subcommittee",
            "Standards",
            "Simulation",
            "methods",
        )
    CREATION_ORGANIZATION_AND_SET_WELL_3_D_INTEROPERABILITY_PARTNERSHIPS_OTHER = (
            "creation",
            "Organization",
            "and",
            "set",
            "well",
            "3D",
            "interoperability",
            "partnerships",
            "other",
        )
    OF_AUTOMATICALLY_XSLT_XPATH_WIDESPREAD_APIS_IF_COMMUNICATION_THOSE_W3_C = (
            "of",
            "automatically",
            "XSLT/Xpath",
            "widespread",
            "APIs",
            "if",
            "communication",
            "those",
            "W3C",
        )


@dataclass
class NistschemaSvIvListStringEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-string-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-string-enumeration-4-NS"

    value: Optional[NistschemaSvIvListStringEnumeration4Type] = field(
        default=None
    )
