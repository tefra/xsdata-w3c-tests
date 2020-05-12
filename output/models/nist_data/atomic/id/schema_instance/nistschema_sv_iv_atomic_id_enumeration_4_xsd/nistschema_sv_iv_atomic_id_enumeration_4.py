from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-4-NS"


class NistschemaSvIvAtomicIdEnumeration4Type(Enum):
    """
    :cvar FOR_NEWCOMERS_FOR_RESOURCES_FORUM_AND_THAN_MAINTAINED_SERIES:
    :cvar HI:
    :cvar IIMPACT_THE_DEVICES_TEMPLATES_SY:
    :cvar LPROVIDES_DISCOVER_OVER_CLEAN_REL:
    :cvar NSOFTWARE_THE_FROM_COMMERCE_USING:
    :cvar QBAN:
    :cvar STESTING_ADDRESSING_TH:
    :cvar WREGISTRIES_RESULT_MADE_KEY_THE_OF_WITHOUT_THE_CAN_ORGANIZATIO:
    """
    FOR_NEWCOMERS_FOR_RESOURCES_FORUM_AND_THAN_MAINTAINED_SERIES = "_for.newcomers_for-resources.forum_and-than.maintained-series-"
    HI = "hi"
    IIMPACT_THE_DEVICES_TEMPLATES_SY = "iimpact-the.devices_templates_sy"
    LPROVIDES_DISCOVER_OVER_CLEAN_REL = "lprovides.discover.over.clean.rel"
    NSOFTWARE_THE_FROM_COMMERCE_USING = "nsoftware.the.from_commerce_using-"
    QBAN = "qban"
    STESTING_ADDRESSING_TH = "stesting-addressing_th"
    WREGISTRIES_RESULT_MADE_KEY_THE_OF_WITHOUT_THE_CAN_ORGANIZATIO = "wregistries_result_made_key.the.of_without_the.can.organizatio"


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-4-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicIdEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicIdEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
