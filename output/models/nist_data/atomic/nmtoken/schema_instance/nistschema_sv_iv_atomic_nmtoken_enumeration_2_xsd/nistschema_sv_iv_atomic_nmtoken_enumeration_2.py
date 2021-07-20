from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-2-NS"


class NistschemaSvIvAtomicNmtokenEnumeration2Type(Enum):
    LED_BACK_MUST_ITL_APPLICATIONS_EXCHA = "led:back:must.ITL_applications:excha"
    AND_SOFTWARE_HELP_BE_SHIFT_OFFER_DOM_WORKING_AUTOMATE_CO = "and-software.help.be:shift:offer.DOM.working.automate:Co"
    COST_ON_AND_AVAILABLE_WILL_TO_MUST_TUNE_CREATI = "cost:on:and_available-will.to:must.tune:creati"
    AS_TEST_MARKUP_SUPPLY_TRANSACTIONS_FOR_STANDARDS_FOR_WITH_SIG = "as:test-Markup-supply.transactions_for_Standards.for-with.sig"
    OUTFITTING_DONAT = "outfitting.donat"
    AND_TO_SIMULATION_PRO = "and-to:Simulation:pro"
    WORKING_SOLVE = "working.solve-"


@dataclass
class NistschemaSvIvAtomicNmtokenEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicNmtokenEnumeration2Type] = field(
        default=None
    )
