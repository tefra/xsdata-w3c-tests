from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-enumeration-3-NS"


class NistschemaSvIvListNormalizedStringEnumeration3Type(Enum):
    """
    :cvar BETTER_COMPUTING_OF_SUPPLY_DISCOVERY:
    :cvar BOTH_THE_AND_INDIVIDUAL_CERTAIN_SUCH_AD_TO_SPECIFICATION:
    :cvar IT_OASIS_BEING_ORGANIZATIONS_THAT:
    :cvar LAW_WILL_AND_APPLICATION_IS_OFFER_HETEROGENEOUS_AUTOMATE:
    :cvar SAME_AND_G_WORKING_INFORMATION:
    :cvar TO_FOR_SUPPLY_OF_BY_REVIEW_INDUSTRY_AND:
    :cvar WEB_CREATION_OF_THE_AND_GRAPHICAL_HIGH_ELIMINATED:
    """
    BETTER_COMPUTING_OF_SUPPLY_DISCOVERY = "better computing of supply discovery"
    BOTH_THE_AND_INDIVIDUAL_CERTAIN_SUCH_AD_TO_SPECIFICATION = "both the and individual certain such ad to specification"
    IT_OASIS_BEING_ORGANIZATIONS_THAT = "it OASIS being organizations that"
    LAW_WILL_AND_APPLICATION_IS_OFFER_HETEROGENEOUS_AUTOMATE = "law will and application is offer heterogeneous automate"
    SAME_AND_G_WORKING_INFORMATION = "same and g Working information"
    TO_FOR_SUPPLY_OF_BY_REVIEW_INDUSTRY_AND = "to for supply of by review industry and"
    WEB_CREATION_OF_THE_AND_GRAPHICAL_HIGH_ELIMINATED = "web creation of the and graphical high eliminated"


@dataclass
class NistschemaSvIvListNormalizedStringEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-normalizedString-enumeration-3-NS"

    value: Optional[NistschemaSvIvListNormalizedStringEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
