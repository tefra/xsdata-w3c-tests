from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-2-NS"


class NistschemaSvIvAtomicNmtokenEnumeration2Type(Enum):
    """
    :cvar AND_SOFTWARE_HELP_BE_SHIFT_OFFER_DOM_WORKING_AUTOMATE_CO:
    :cvar AND_TO_SIMULATION_PRO:
    :cvar AS_TEST_MARKUP_SUPPLY_TRANSACTIONS_FOR_STANDARDS_FOR_WITH_SIG:
    :cvar COST_ON_AND_AVAILABLE_WILL_TO_MUST_TUNE_CREATI:
    :cvar LED_BACK_MUST_ITL_APPLICATIONS_EXCHA:
    :cvar OUTFITTING_DONAT:
    :cvar WORKING_SOLVE:
    """
    AND_SOFTWARE_HELP_BE_SHIFT_OFFER_DOM_WORKING_AUTOMATE_CO = "and-software.help.be:shift:offer.DOM.working.automate:Co"
    AND_TO_SIMULATION_PRO = "and-to:Simulation:pro"
    AS_TEST_MARKUP_SUPPLY_TRANSACTIONS_FOR_STANDARDS_FOR_WITH_SIG = "as:test-Markup-supply.transactions_for_Standards.for-with.sig"
    COST_ON_AND_AVAILABLE_WILL_TO_MUST_TUNE_CREATI = "cost:on:and_available-will.to:must.tune:creati"
    LED_BACK_MUST_ITL_APPLICATIONS_EXCHA = "led:back:must.ITL_applications:excha"
    OUTFITTING_DONAT = "outfitting.donat"
    WORKING_SOLVE = "working.solve-"


@dataclass
class NistschemaSvIvAtomicNmtokenEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicNmtokenEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
