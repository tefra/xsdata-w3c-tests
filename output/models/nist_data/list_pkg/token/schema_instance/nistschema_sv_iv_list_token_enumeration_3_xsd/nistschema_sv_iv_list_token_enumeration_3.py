from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-enumeration-3-NS"


class NistschemaSvIvListTokenEnumeration3Type(Enum):
    """
    :cvar USES_TEMPLATES_TO_IS_THE:
    :cvar AND_SERVICE_WILL_OPPORTUNITY_THE:
    :cvar AND_HAS_EMBEDDED_FILES_WOULD_INCORPORATED_INTEROPERABILITY_OBJECTIVE_HETEROGENEOUS:
    :cvar TO_TEST_MANIPULATION_MODELS_PROMINENT_OF_AND:
    :cvar IT_TO_OF_CHALLENGES_FOR_AND_CAN_CONSTITUENT_DEVICES:
    :cvar FOR_G_NEW_PARTNERSHIP_TOOLS:
    :cvar BE_BUILD_XML_DATA_S_THE_DOCUMENTS_INDUSTRY:
    """
    USES_TEMPLATES_TO_IS_THE = "uses templates to is The"
    AND_SERVICE_WILL_OPPORTUNITY_THE = "and service will opportunity the"
    AND_HAS_EMBEDDED_FILES_WOULD_INCORPORATED_INTEROPERABILITY_OBJECTIVE_HETEROGENEOUS = "and has embedded files would incorporated interoperability objective heterogeneous"
    TO_TEST_MANIPULATION_MODELS_PROMINENT_OF_AND = "to test manipulation models prominent of and"
    IT_TO_OF_CHALLENGES_FOR_AND_CAN_CONSTITUENT_DEVICES = "it to of challenges for and can constituent devices"
    FOR_G_NEW_PARTNERSHIP_TOOLS = "for g new partnership tools"
    BE_BUILD_XML_DATA_S_THE_DOCUMENTS_INDUSTRY = "be build XML data; s The documents industry"


@dataclass
class NistschemaSvIvListTokenEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-token-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-token-enumeration-3-NS"

    value: Optional[NistschemaSvIvListTokenEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
