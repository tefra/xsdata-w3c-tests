from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-enumeration-5-NS"


class NistschemaSvIvListStringEnumeration5Type(Enum):
    """
    :cvar BECOME_TO_XML_THAT_WILL_THE_PICO_CELLULAR_CROSS_OVER_MARKET_IMPACT:
    :cvar CAN_NSRL_PROMISES_DATA_XML_ACTING:
    :cvar PROVIDES_PROVIDE_HIGHLY_INDUSTRY_ANY_ON_TOOLS_WITH_FOR:
    :cvar SPECIFICATIONS_BUILD_FOR_THE_WILL_WEB:
    :cvar TEST_FURTHERMORE_AND_DOCUMENTS_AS_BE:
    :cvar TO_E_XTENSIBLE_CAN_IS_INFORMATION_ASPECTS_STANDARD:
    """
    BECOME_TO_XML_THAT_WILL_THE_PICO_CELLULAR_CROSS_OVER_MARKET_IMPACT = "become to XML that will the pico-cellular cross-over market impact"
    CAN_NSRL_PROMISES_DATA_XML_ACTING = "can NSRL promises data; XML acting"
    PROVIDES_PROVIDE_HIGHLY_INDUSTRY_ANY_ON_TOOLS_WITH_FOR = "provides Provide highly industry any on tools with for"
    SPECIFICATIONS_BUILD_FOR_THE_WILL_WEB = "specifications build for the will web"
    TEST_FURTHERMORE_AND_DOCUMENTS_AS_BE = "test Furthermore and documents as be"
    TO_E_XTENSIBLE_CAN_IS_INFORMATION_ASPECTS_STANDARD = "to eXtensible can is information aspects standard"


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
