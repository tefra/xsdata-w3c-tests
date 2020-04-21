from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-enumeration-5-NS"


class NistschemaSvIvListTokenEnumeration5Type(Enum):
    """
    :cvar AN_OBJECT_AND_IMPLEMENTATION_ABOUT_ORIGINAL_FROM_INFORMATION:
    :cvar LANGUAGE_INDUSTRY_THE_INFORMATION_WITH_ADDRESSING_DYNAMIC_TECHNICAL_ADDITIONALLY:
    :cvar NSRL_WITH_AND_CONSEQUENTLY_DATA:
    :cvar AND_DOMAINS_INTEROPERABILITY_LED_OUTFITTING_SPECIFICATIONS_RECOMMENDATIONS:
    :cvar CONFORMANCE_SIGNATURE_DEVICES_THE_OTHER_AND_STANDARDS:
    :cvar EACH_ALLOW_OVER_APPLICATIONS_INTERNET_TECHNICAL_TO:
    :cvar OF_COMMUNITY_INTEROPERABILITY_AND_DATA_INFORMATION_ALL_THESE:
    :cvar THE_IN_CREATE_TO_ENFORCEMENT_UNBIASED_XML:
    :cvar UNDERSTAND_TOOLS_OF_INTEROPERABLE_XML_FOR:
    """
    AN_OBJECT_AND_IMPLEMENTATION_ABOUT_ORIGINAL_FROM_INFORMATION = "An object and implementation about original from information"
    LANGUAGE_INDUSTRY_THE_INFORMATION_WITH_ADDRESSING_DYNAMIC_TECHNICAL_ADDITIONALLY = "Language industry the Information with addressing dynamic Technical additionally"
    NSRL_WITH_AND_CONSEQUENTLY_DATA = "NSRL with and Consequently data;"
    AND_DOMAINS_INTEROPERABILITY_LED_OUTFITTING_SPECIFICATIONS_RECOMMENDATIONS = "and domains interoperability led outfitting specifications Recommendations"
    CONFORMANCE_SIGNATURE_DEVICES_THE_OTHER_AND_STANDARDS = "conformance signature devices the other and Standards"
    EACH_ALLOW_OVER_APPLICATIONS_INTERNET_TECHNICAL_TO = "each allow over applications Internet technical to"
    OF_COMMUNITY_INTEROPERABILITY_AND_DATA_INFORMATION_ALL_THESE = "of Community interoperability and data information all these"
    THE_IN_CREATE_TO_ENFORCEMENT_UNBIASED_XML = "the in create to enforcement: unbiased XML"
    UNDERSTAND_TOOLS_OF_INTEROPERABLE_XML_FOR = "understand tools of interoperable XML for"


@dataclass
class NistschemaSvIvListTokenEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-token-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-token-enumeration-5-NS"

    value: Optional[NistschemaSvIvListTokenEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
