from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-enumeration-4-NS"


class NistschemaSvIvListStringEnumeration4Type(Enum):
    """
    :cvar A_THE_SUPPLY_THE_AND_POPULAR_UNBIASED:
    :cvar AND_DEVELOPING_OBJECT_NSRL_MAINTAINED_MEETS_THE_IMPLEMENTATIONS_MANIPULATE:
    :cvar CREATION_ORGANIZATION_AND_SET_WELL_3_D_INTEROPERABILITY_PARTNERSHIPS_OTHER:
    :cvar INVESTIGATION_TO_THE_CAPABILITIES_THEM:
    :cvar MANIPULATE_IS_THIS_OF_WOULD_BUILT_FOR_USE:
    :cvar OF_AUTOMATICALLY_XSLT_XPATH_WIDESPREAD_APIS_IF_COMMUNICATION_THOSE_W3_C:
    :cvar ORGANIZATIONS_SCREEN_SUBCOMMITTEE_STANDARDS_SIMULATION_METHODS:
    """
    A_THE_SUPPLY_THE_AND_POPULAR_UNBIASED = "a The supply the and popular unbiased"
    AND_DEVELOPING_OBJECT_NSRL_MAINTAINED_MEETS_THE_IMPLEMENTATIONS_MANIPULATE = "and developing object NSRL maintained meets the implementations manipulate"
    CREATION_ORGANIZATION_AND_SET_WELL_3_D_INTEROPERABILITY_PARTNERSHIPS_OTHER = "creation Organization and set well 3D interoperability partnerships other"
    INVESTIGATION_TO_THE_CAPABILITIES_THEM = "investigation to the capabilities them"
    MANIPULATE_IS_THIS_OF_WOULD_BUILT_FOR_USE = "manipulate is this of would built for use"
    OF_AUTOMATICALLY_XSLT_XPATH_WIDESPREAD_APIS_IF_COMMUNICATION_THOSE_W3_C = "of automatically XSLT/Xpath widespread APIs if communication those W3C"
    ORGANIZATIONS_SCREEN_SUBCOMMITTEE_STANDARDS_SIMULATION_METHODS = "organizations screen Subcommittee Standards Simulation methods"


@dataclass
class NistschemaSvIvListStringEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-string-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-string-enumeration-4-NS"

    value: Optional[NistschemaSvIvListStringEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
