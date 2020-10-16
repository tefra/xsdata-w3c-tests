from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-enumeration-2-NS"


class NistschemaSvIvListTokenEnumeration2Type(Enum):
    """
    :cvar INVESTIGATIONS_THE_NIST_ITL_INDUSTRY_EFFECTIVELY_FOR_TO_AND_XML:
    :cvar AND_FOCUSING_INTO_COMPLETION_OBJECTIVE:
    :cvar MEDIUM_SIZED_TESTING_INVESTIGATION_CHOICES_FOSTER:
    :cvar SPECIFICATION_FOR_000_BUSINESS_INVESTIGATION_FIRST_GENERATION_THE_SPECIFICATIONS_BE:
    :cvar THE_FOR_KNOWN_PERFORMANCE_LIBRARY_COMPLEX_FILE_ABILITY_SEMANTICS:
    :cvar BUSINESS_XSL_FO_ALL_DEVELOPMENT_ISSUES_XML_TO_ALSO:
    """
    INVESTIGATIONS_THE_NIST_ITL_INDUSTRY_EFFECTIVELY_FOR_TO_AND_XML = "investigations the NIST/ITL industry effectively for To and XML"
    AND_FOCUSING_INTO_COMPLETION_OBJECTIVE = "and focusing into completion objective"
    MEDIUM_SIZED_TESTING_INVESTIGATION_CHOICES_FOSTER = "medium-sized testing Investigation choices foster"
    SPECIFICATION_FOR_000_BUSINESS_INVESTIGATION_FIRST_GENERATION_THE_SPECIFICATIONS_BE = "specification for 000 business investigation first-generation the specifications be"
    THE_FOR_KNOWN_PERFORMANCE_LIBRARY_COMPLEX_FILE_ABILITY_SEMANTICS = "the for known performance library complex file ability semantics"
    BUSINESS_XSL_FO_ALL_DEVELOPMENT_ISSUES_XML_TO_ALSO = "business XSL-FO all development issues XML to also"


@dataclass
class NistschemaSvIvListTokenEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-token-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-token-enumeration-2-NS"

    value: Optional[NistschemaSvIvListTokenEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
