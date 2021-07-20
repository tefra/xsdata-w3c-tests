from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-enumeration-1-NS"


class NistschemaSvIvAtomicNcnameEnumeration1Type(Enum):
    IS_TESTING_REGISTRY_FOR_COME_POPULAR_NETWORKING_IS_BETWE = "_is-testing.registry_for_come_popular-networking-is-betwe"
    RIS_BOTH_INCLUDING_INDUSTRIES_SOFTWARE_WHICH_STAK = "ris.both-including-industries_software.which-stak"
    COF_A_RETRIEVE_CONTAINED_INTO_FOR_INDU = "cof-a-retrieve-contained_into_for.indu"
    VWITH_COMPUTERS_DISCUSSIONS_APPLIC = "vwith.computers_discussions.applic"
    EW = "ew"
    IS_KNOWN_MUST_MANIPULATE_TO_REFER = "_is-known.must_manipulate-to_refer"
    GA_THE_THE = "ga.the_the"
    HA_AD_PROTOTYPE_LED_PROCESS_OTHER_OF_SPECIFICATIONS_APPROPRIAT = "ha_ad_prototype_led.process_other-of.specifications_appropriat"


@dataclass
class NistschemaSvIvAtomicNcnameEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-NCName-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicNcnameEnumeration1Type] = field(
        default=None
    )
