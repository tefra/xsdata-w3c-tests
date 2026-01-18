from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-enumeration-4-NS"


class NistschemaSvIvListNormalizedStringEnumeration4Type(Enum):
    BROWSERS_TARGETED_FROM_DO_UNITED_CONSEQUENTLY = (
        "browsers",
        "targeted",
        "from",
        "do",
        "United",
        "Consequently",
    )
    XML_RELATED_THE_WITHIN_DATABASE_YEARS = (
        "XML-related",
        "the",
        "within",
        "database",
        "years",
    )
    NIST_STANDARDIZATION_TECHNOLOGIES_TECHNOLOGY_TO_FOR_CREATION = (
        "NIST",
        "standardization",
        "technologies",
        "technology",
        "to",
        "for",
        "creation",
    )
    ACCESSIBLE_TOOLS_PARTICULARLY_MEDIUMS_DRAFT = (
        "accessible",
        "tools",
        "particularly",
        "mediums",
        "draft",
    )
    XML_ARE_LEADERSHIP_TARGET_INDIVIDUAL_HELP_FILES = (
        "XML",
        "are",
        "leadership",
        "target",
        "individual",
        "help",
        "files",
    )
    DESIGN_WITH_MUST_XML_ENSURE_TO_THEM_ABLE = (
        "design",
        "with",
        "must",
        "XML",
        "ensure",
        "to",
        "them",
        "able",
    )
    IDENTIFY_THAT_FUTURE_CREATES_SYSTEM = (
        "identify",
        "that",
        "future",
        "creates",
        "system",
    )
    ABILITY_REGISTRY_REPOSITORY_DATA_AND_NIST_ITL_20_BENEFITS_THEM_BUSINESS = (
        "ability",
        "Registry/Repository",
        "data;",
        "and",
        "NIST/ITL",
        "20",
        "benefits",
        "them",
        "business",
    )
    NIST_ITL_TO_THAT_INDUSTRY_FOR_WHICH = (
        "NIST/ITL",
        "to",
        "that",
        "industry",
        "for",
        "which",
    )


@dataclass(kw_only=True)
class NistschemaSvIvListNormalizedStringEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-normalizedString-enumeration-4-NS"

    value: NistschemaSvIvListNormalizedStringEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
