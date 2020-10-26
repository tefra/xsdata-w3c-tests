from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-enumeration-5-NS"


class NistschemaSvIvListNormalizedStringEnumeration5Type(Enum):
    """
    :cvar WITH_THE_OF_XML_INTERCONNECTING_MAINTAINS:
    :cvar AT_NIST_ITL_IS_OPPORTUNITY_CONCEPTS:
    :cvar HELPING_AND_SOFTWARE_THEN_ALLOWS_CONFERENCE_COMPLEX_STANDARDS_NETWORKING:
    :cvar ALIKE_ON_CAPABILITIES_EFFECTIVELY_NUMBER_XML_AND_LED_LANDSCAPE:
    :cvar CONSORTIUMS_FACILITATION_OF_TO_XSLT_XPATH:
    :cvar COME_BUILD_ENVIRONMENTS_AND_SUCH_EMERGING_USING_OF:
    :cvar S_ACHIEVED_CONTRIBUTOR_AND_ELECTRONIC:
    :cvar UNAMBIGUOUS_PARADIGM_THE_SET_THE_FROM_FOR_ONE:
    :cvar ADVENT_SCREEN_REPOSITORY_BETTER_YEARS:
    :cvar THE_NETWORKING_MUST_DISTRIBUTED_SPECIFICATION_OF_UNDERSTAND:
    """
    WITH_THE_OF_XML_INTERCONNECTING_MAINTAINS = "with the of XML interconnecting maintains"
    AT_NIST_ITL_IS_OPPORTUNITY_CONCEPTS = "at NIST/ITL is opportunity concepts"
    HELPING_AND_SOFTWARE_THEN_ALLOWS_CONFERENCE_COMPLEX_STANDARDS_NETWORKING = "helping and software then allows Conference complex standards networking"
    ALIKE_ON_CAPABILITIES_EFFECTIVELY_NUMBER_XML_AND_LED_LANDSCAPE = "alike on capabilities effectively number XML and led landscape"
    CONSORTIUMS_FACILITATION_OF_TO_XSLT_XPATH = "consortiums Facilitation of to XSLT/Xpath"
    COME_BUILD_ENVIRONMENTS_AND_SUCH_EMERGING_USING_OF = "come build environments and such emerging Using of"
    S_ACHIEVED_CONTRIBUTOR_AND_ELECTRONIC = "s achieved contributor and Electronic"
    UNAMBIGUOUS_PARADIGM_THE_SET_THE_FROM_FOR_ONE = "unambiguous paradigm the set The from for One"
    ADVENT_SCREEN_REPOSITORY_BETTER_YEARS = "advent screen repository better years"
    THE_NETWORKING_MUST_DISTRIBUTED_SPECIFICATION_OF_UNDERSTAND = "the networking must distributed specification of understand"


@dataclass
class NistschemaSvIvListNormalizedStringEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-normalizedString-enumeration-5-NS"

    value: Optional[NistschemaSvIvListNormalizedStringEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
