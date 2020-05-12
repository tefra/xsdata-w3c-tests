from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-enumeration-4-NS"


class NistschemaSvIvListNormalizedStringEnumeration4Type(Enum):
    """
    :cvar ABILITY_REGISTRY_REPOSITORY_DATA_AND_NIST_ITL_20_BENEFITS_THEM_BUSINESS:
    :cvar ACCESSIBLE_TOOLS_PARTICULARLY_MEDIUMS_DRAFT:
    :cvar BROWSERS_TARGETED_FROM_DO_UNITED_CONSEQUENTLY:
    :cvar DESIGN_WITH_MUST_XML_ENSURE_TO_THEM_ABLE:
    :cvar IDENTIFY_THAT_FUTURE_CREATES_SYSTEM:
    :cvar NIST_ITL_TO_THAT_INDUSTRY_FOR_WHICH:
    :cvar NIST_STANDARDIZATION_TECHNOLOGIES_TECHNOLOGY_TO_FOR_CREATION:
    :cvar XML_ARE_LEADERSHIP_TARGET_INDIVIDUAL_HELP_FILES:
    :cvar XML_RELATED_THE_WITHIN_DATABASE_YEARS:
    """
    ABILITY_REGISTRY_REPOSITORY_DATA_AND_NIST_ITL_20_BENEFITS_THEM_BUSINESS = "ability Registry/Repository data; and NIST/ITL 20 benefits them business"
    ACCESSIBLE_TOOLS_PARTICULARLY_MEDIUMS_DRAFT = "accessible tools particularly mediums draft"
    BROWSERS_TARGETED_FROM_DO_UNITED_CONSEQUENTLY = "browsers targeted from do United Consequently"
    DESIGN_WITH_MUST_XML_ENSURE_TO_THEM_ABLE = "design with must XML ensure to them able"
    IDENTIFY_THAT_FUTURE_CREATES_SYSTEM = "identify that future creates system"
    NIST_ITL_TO_THAT_INDUSTRY_FOR_WHICH = "NIST/ITL to that industry for which"
    NIST_STANDARDIZATION_TECHNOLOGIES_TECHNOLOGY_TO_FOR_CREATION = "NIST standardization technologies technology to for creation"
    XML_ARE_LEADERSHIP_TARGET_INDIVIDUAL_HELP_FILES = "XML are leadership target individual help files"
    XML_RELATED_THE_WITHIN_DATABASE_YEARS = "XML-related the within database years"


@dataclass
class NistschemaSvIvListNormalizedStringEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-normalizedString-enumeration-4-NS"

    value: Optional[NistschemaSvIvListNormalizedStringEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
