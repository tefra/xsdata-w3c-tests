from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-enumeration-1-NS"


class NistschemaSvIvListNormalizedStringEnumeration1Type(Enum):
    """
    :cvar THE_CPU_NOT_TO_WITH_TOOLS_XML_AND_THE:
    :cvar XSL_NIST_ITL_WORLD_SOFTWARE_DEFINE_AROMA_TESTABLE_RELATED:
    :cvar BECOME_WITH_COST_INCLUDING_CONTRIBUTE_MEASURE_SOFTWARE_DEBUG:
    :cvar DOCUMENTS_OUR_IN_LANGUAGE_AND_LED:
    :cvar FOR_TWO_IN_HOUSE_THE_PARTNERSHIPS_DATA_INVESTIGATION_COMPUTING_EMERGING:
    :cvar SPECIFICATIONS_DEVELOPMENT_SHIFT_WAYS_COMPUTING:
    :cvar TECHNOLOGY_BUSINESS_INDUSTRY_VERSIONS_NIST_ITL_BY_ALL_DEVELOPERS:
    :cvar TESTING_THE_DEPENDS_BE_BUSINESS_AND_SIGNATURES:
    :cvar TOOLS_DESKTOP_KNOWN_FOR_CAN_CORRECTNESS_AS_THE_MARKET:
    :cvar WIDESPREAD_OASIS_AND_IN_HOUSE_AUTOMATING_OF:
    """
    THE_CPU_NOT_TO_WITH_TOOLS_XML_AND_THE = "The CPU not to with tools XML and the"
    XSL_NIST_ITL_WORLD_SOFTWARE_DEFINE_AROMA_TESTABLE_RELATED = "XSL NIST/ITL world software define Aroma testable related"
    BECOME_WITH_COST_INCLUDING_CONTRIBUTE_MEASURE_SOFTWARE_DEBUG = "become with cost including contribute measure software debug"
    DOCUMENTS_OUR_IN_LANGUAGE_AND_LED = "documents our in language and led"
    FOR_TWO_IN_HOUSE_THE_PARTNERSHIPS_DATA_INVESTIGATION_COMPUTING_EMERGING = "for two in-house The partnerships data Investigation computing emerging"
    SPECIFICATIONS_DEVELOPMENT_SHIFT_WAYS_COMPUTING = "specifications development shift ways computing"
    TECHNOLOGY_BUSINESS_INDUSTRY_VERSIONS_NIST_ITL_BY_ALL_DEVELOPERS = "technology business industry versions NIST/ITL by all developers"
    TESTING_THE_DEPENDS_BE_BUSINESS_AND_SIGNATURES = "testing the depends be business and signatures"
    TOOLS_DESKTOP_KNOWN_FOR_CAN_CORRECTNESS_AS_THE_MARKET = "tools desktop known for can correctness as the market"
    WIDESPREAD_OASIS_AND_IN_HOUSE_AUTOMATING_OF = "widespread OASIS and in-house automating of"


@dataclass
class NistschemaSvIvListNormalizedStringEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-normalizedString-enumeration-1-NS"

    value: Optional[NistschemaSvIvListNormalizedStringEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )