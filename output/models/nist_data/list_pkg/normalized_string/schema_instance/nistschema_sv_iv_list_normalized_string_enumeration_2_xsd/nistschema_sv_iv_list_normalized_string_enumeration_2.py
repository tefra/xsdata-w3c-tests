from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-enumeration-2-NS"


class NistschemaSvIvListNormalizedStringEnumeration2Type(Enum):
    """
    :cvar DESPITE_SPECIFICATIONS_OF_SUCH_THIS_AN_WITH_DEFINES:
    :cvar FURTHERMORE_AS_WITHOUT_2000_AND_INDUSTRY_IS_OVER_FOR:
    :cvar ASSURING_TO_COMPLETION_AND_REGISTRY_REPOSITORY_WITH_FOR_HAVE:
    :cvar BUSINESS_PERVASIVE_AND_AVAILABLE_OF:
    :cvar DATA_INDUSTRIES_FOR_CREATION_INFLUENCE:
    :cvar MANY_POPULAR_NOT_IN_ARE_THE:
    :cvar REGISTRY_REPOSITORY_EB_XML_BE_THESE_AUTOMATE_UTILIZE_CROSS_REFERENCE_THAT:
    :cvar WORLD_PROVIDE_THE_TECHNOLOGIES_SPECIFICATIONS_MARKET_NEEDS:
    """
    DESPITE_SPECIFICATIONS_OF_SUCH_THIS_AN_WITH_DEFINES = "Despite specifications of such this an with defines"
    FURTHERMORE_AS_WITHOUT_2000_AND_INDUSTRY_IS_OVER_FOR = "Furthermore as without 2000 and industry is over for"
    ASSURING_TO_COMPLETION_AND_REGISTRY_REPOSITORY_WITH_FOR_HAVE = "assuring to completion and registry/repository with for have"
    BUSINESS_PERVASIVE_AND_AVAILABLE_OF = "business pervasive and available of"
    DATA_INDUSTRIES_FOR_CREATION_INFLUENCE = "data industries for creation influence"
    MANY_POPULAR_NOT_IN_ARE_THE = "many popular not in are the"
    REGISTRY_REPOSITORY_EB_XML_BE_THESE_AUTOMATE_UTILIZE_CROSS_REFERENCE_THAT = "registry/repository ebXML; be these automate utilize cross-reference that"
    WORLD_PROVIDE_THE_TECHNOLOGIES_SPECIFICATIONS_MARKET_NEEDS = "world Provide the technologies specifications market needs"


@dataclass
class NistschemaSvIvListNormalizedStringEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-normalizedString-enumeration-2-NS"

    value: Optional[NistschemaSvIvListNormalizedStringEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )