from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-enumeration-2-NS"


class NistschemaSvIvListNormalizedStringEnumeration2Type(Enum):
    FURTHERMORE_AS_WITHOUT_2000_AND_INDUSTRY_IS_OVER_FOR = (
        "Furthermore",
        "as",
        "without",
        "2000",
        "and",
        "industry",
        "is",
        "over",
        "for",
    )
    REGISTRY_REPOSITORY_EB_XML_BE_THESE_AUTOMATE_UTILIZE_CROSS_REFERENCE_THAT = (
        "registry/repository",
        "ebXML;",
        "be",
        "these",
        "automate",
        "utilize",
        "cross-reference",
        "that",
    )
    DATA_INDUSTRIES_FOR_CREATION_INFLUENCE = (
        "data",
        "industries",
        "for",
        "creation",
        "influence",
    )
    ASSURING_TO_COMPLETION_AND_REGISTRY_REPOSITORY_WITH_FOR_HAVE = (
        "assuring",
        "to",
        "completion",
        "and",
        "registry/repository",
        "with",
        "for",
        "have",
    )
    MANY_POPULAR_NOT_IN_ARE_THE = (
        "many",
        "popular",
        "not",
        "in",
        "are",
        "the",
    )
    BUSINESS_PERVASIVE_AND_AVAILABLE_OF = (
        "business",
        "pervasive",
        "and",
        "available",
        "of",
    )
    DESPITE_SPECIFICATIONS_OF_SUCH_THIS_AN_WITH_DEFINES = (
        "Despite",
        "specifications",
        "of",
        "such",
        "this",
        "an",
        "with",
        "defines",
    )
    WORLD_PROVIDE_THE_TECHNOLOGIES_SPECIFICATIONS_MARKET_NEEDS = (
        "world",
        "Provide",
        "the",
        "technologies",
        "specifications",
        "market",
        "needs",
    )


@dataclass(kw_only=True)
class NistschemaSvIvListNormalizedStringEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-normalizedString-enumeration-2-NS"

    value: NistschemaSvIvListNormalizedStringEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
