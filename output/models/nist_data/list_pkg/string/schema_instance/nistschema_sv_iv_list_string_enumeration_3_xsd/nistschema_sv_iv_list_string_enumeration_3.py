from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-enumeration-3-NS"


class NistschemaSvIvListStringEnumeration3Type(Enum):
    """
    :cvar LANGUAGE_INDUSTRY_EXTENSIBLE_THE_WHICH_TOOLS_THE_RELATED_BE:
    :cvar REGISTRY_REPOSITORY_LANGUAGE_PARTNERS_CAN_DISCOVERY_DOM_THIS_ARE:
    :cvar INDUSTRY_SUBCOMMITTEE_OBJECT_VISIBLY_USED_FOR_MEASURE:
    :cvar MEET_BETA_TOOLS_BY_LACKING_AND_CHALLENGES:
    :cvar OF_ISSUES_BUSINESS_ORIENTED_PC_AS_IN_HOUSE_TYPICAL:
    :cvar OF_MADE_DISCOVERY_OWN_APPROPRIATE:
    :cvar SOFTWARE_DIGITAL_SOFTWARE_NEED_AND_ISSUES:
    """
    LANGUAGE_INDUSTRY_EXTENSIBLE_THE_WHICH_TOOLS_THE_RELATED_BE = "Language industry Extensible the which tools The related be"
    REGISTRY_REPOSITORY_LANGUAGE_PARTNERS_CAN_DISCOVERY_DOM_THIS_ARE = "Registry/Repository language partners can discovery DOM this are"
    INDUSTRY_SUBCOMMITTEE_OBJECT_VISIBLY_USED_FOR_MEASURE = "industry Subcommittee object visibly used for measure"
    MEET_BETA_TOOLS_BY_LACKING_AND_CHALLENGES = "meet beta tools by lacking and challenges"
    OF_ISSUES_BUSINESS_ORIENTED_PC_AS_IN_HOUSE_TYPICAL = "of issues business-oriented PC as in-house typical"
    OF_MADE_DISCOVERY_OWN_APPROPRIATE = "of made discovery own appropriate"
    SOFTWARE_DIGITAL_SOFTWARE_NEED_AND_ISSUES = "software digital Software need and issues"


@dataclass
class NistschemaSvIvListStringEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-string-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-string-enumeration-3-NS"

    value: Optional[NistschemaSvIvListStringEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
