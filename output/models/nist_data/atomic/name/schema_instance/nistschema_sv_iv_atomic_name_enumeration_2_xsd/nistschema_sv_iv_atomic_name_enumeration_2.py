from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-2-NS"


class NistschemaSvIvAtomicNameEnumeration2Type(Enum):
    """
    :cvar UOF_RETRIEVE_THE_PROVIDED_SPECIFIC_IN_SYSTEMS_ON_A_CHI:
    :cvar PIS_KNOWN_OVER_ALLOW:
    :cvar DISCOVERY_DESIGNED_GRAPHICS_PERV:
    :cvar JREGISTRY_INTEROPERABILITY_HAMPERED_O:
    :cvar GREAT_DESK:
    :cvar RA_THE_PARTNERS_THAT_PERVASIVE_BY_CHALLENGES_DISCOVER:
    :cvar PNEXT_CREAT:
    :cvar YR:
    """
    UOF_RETRIEVE_THE_PROVIDED_SPECIFIC_IN_SYSTEMS_ON_A_CHI = "uof.retrieve:the_provided_specific_in_systems-on-a-chi"
    PIS_KNOWN_OVER_ALLOW = "pis_known:over.allow."
    DISCOVERY_DESIGNED_GRAPHICS_PERV = "_discovery:designed_graphics_perv"
    JREGISTRY_INTEROPERABILITY_HAMPERED_O = "jregistry.interoperability_hampered-o"
    GREAT_DESK = "_great-desk"
    RA_THE_PARTNERS_THAT_PERVASIVE_BY_CHALLENGES_DISCOVER = "ra-the-partners-that-pervasive.by_challenges:discover"
    PNEXT_CREAT = "pnext:creat"
    YR = "yr"


@dataclass
class NistschemaSvIvAtomicNameEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-Name-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicNameEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
