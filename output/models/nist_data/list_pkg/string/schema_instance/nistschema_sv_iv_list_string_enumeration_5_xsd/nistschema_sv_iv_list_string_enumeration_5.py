from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-enumeration-5-NS"


class NistschemaSvIvListStringEnumeration5Type(Enum):
    """
    :cvar PROVIDES_PROVIDE_HIGHLY_INDUSTRY_ANY_ON_TOOLS_WITH_FOR:
    :cvar TO_E_XTENSIBLE_CAN_IS_INFORMATION_ASPECTS_STANDARD:
    :cvar TEST_FURTHERMORE_AND_DOCUMENTS_AS_BE:
    :cvar CAN_NSRL_PROMISES_DATA_XML_ACTING:
    :cvar BECOME_TO_XML_THAT_WILL_THE_PICO_CELLULAR_CROSS_OVER_MARKET_IMPACT:
    :cvar SPECIFICATIONS_BUILD_FOR_THE_WILL_WEB:
    """
    PROVIDES_PROVIDE_HIGHLY_INDUSTRY_ANY_ON_TOOLS_WITH_FOR = "provides Provide highly industry any on tools with for"
    TO_E_XTENSIBLE_CAN_IS_INFORMATION_ASPECTS_STANDARD = "to eXtensible can is information aspects standard"
    TEST_FURTHERMORE_AND_DOCUMENTS_AS_BE = "test Furthermore and documents as be"
    CAN_NSRL_PROMISES_DATA_XML_ACTING = "can NSRL promises data; XML acting"
    BECOME_TO_XML_THAT_WILL_THE_PICO_CELLULAR_CROSS_OVER_MARKET_IMPACT = "become to XML that will the pico-cellular cross-over market impact"
    SPECIFICATIONS_BUILD_FOR_THE_WILL_WEB = "specifications build for the will web"


@dataclass
class NistschemaSvIvListStringEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-string-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-string-enumeration-5-NS"

    value: Optional[NistschemaSvIvListStringEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
