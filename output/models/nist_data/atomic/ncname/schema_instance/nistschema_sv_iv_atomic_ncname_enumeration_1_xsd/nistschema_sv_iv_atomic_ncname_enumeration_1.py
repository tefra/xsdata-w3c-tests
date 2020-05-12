from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-enumeration-1-NS"


class NistschemaSvIvAtomicNcnameEnumeration1Type(Enum):
    """
    :cvar COF_A_RETRIEVE_CONTAINED_INTO_FOR_INDU:
    :cvar EW:
    :cvar GA_THE_THE:
    :cvar HA_AD_PROTOTYPE_LED_PROCESS_OTHER_OF_SPECIFICATIONS_APPROPRIAT:
    :cvar IS_KNOWN_MUST_MANIPULATE_TO_REFER:
    :cvar IS_TESTING_REGISTRY_FOR_COME_POPULAR_NETWORKING_IS_BETWE:
    :cvar RIS_BOTH_INCLUDING_INDUSTRIES_SOFTWARE_WHICH_STAK:
    :cvar VWITH_COMPUTERS_DISCUSSIONS_APPLIC:
    """
    COF_A_RETRIEVE_CONTAINED_INTO_FOR_INDU = "cof-a-retrieve-contained_into_for.indu"
    EW = "ew"
    GA_THE_THE = "ga.the_the"
    HA_AD_PROTOTYPE_LED_PROCESS_OTHER_OF_SPECIFICATIONS_APPROPRIAT = "ha_ad_prototype_led.process_other-of.specifications_appropriat"
    IS_KNOWN_MUST_MANIPULATE_TO_REFER = "_is-known.must_manipulate-to_refer"
    IS_TESTING_REGISTRY_FOR_COME_POPULAR_NETWORKING_IS_BETWE = "_is-testing.registry_for_come_popular-networking-is-betwe"
    RIS_BOTH_INCLUDING_INDUSTRIES_SOFTWARE_WHICH_STAK = "ris.both-including-industries_software.which-stak"
    VWITH_COMPUTERS_DISCUSSIONS_APPLIC = "vwith.computers_discussions.applic"


@dataclass
class NistschemaSvIvAtomicNcnameEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-NCName-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicNcnameEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
