from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-enumeration-3-NS"


class NistschemaSvIvListNormalizedStringEnumeration3Type(Enum):
    SAME_AND_G_WORKING_INFORMATION = (
        "same",
        "and",
        "g",
        "Working",
        "information",
    )
    BOTH_THE_AND_INDIVIDUAL_CERTAIN_SUCH_AD_TO_SPECIFICATION = (
        "both",
        "the",
        "and",
        "individual",
        "certain",
        "such",
        "ad",
        "to",
        "specification",
    )
    LAW_WILL_AND_APPLICATION_IS_OFFER_HETEROGENEOUS_AUTOMATE = (
        "law",
        "will",
        "and",
        "application",
        "is",
        "offer",
        "heterogeneous",
        "automate",
    )
    WEB_CREATION_OF_THE_AND_GRAPHICAL_HIGH_ELIMINATED = (
        "web",
        "creation",
        "of",
        "the",
        "and",
        "graphical",
        "high",
        "eliminated",
    )
    BETTER_COMPUTING_OF_SUPPLY_DISCOVERY = (
        "better",
        "computing",
        "of",
        "supply",
        "discovery",
    )
    IT_OASIS_BEING_ORGANIZATIONS_THAT = (
        "it",
        "OASIS",
        "being",
        "organizations",
        "that",
    )
    TO_FOR_SUPPLY_OF_BY_REVIEW_INDUSTRY_AND = (
        "to",
        "for",
        "supply",
        "of",
        "by",
        "review",
        "industry",
        "and",
    )


@dataclass
class NistschemaSvIvListNormalizedStringEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-normalizedString-enumeration-3-NS"

    value: Optional[NistschemaSvIvListNormalizedStringEnumeration3Type] = (
        field(
            default=None,
            metadata={
                "required": True,
            },
        )
    )
