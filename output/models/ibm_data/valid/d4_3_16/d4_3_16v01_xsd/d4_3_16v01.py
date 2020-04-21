from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v01"


@dataclass
class Root:
    """
    :ivar el_dtime_type:
    :ivar el_dtime_etprohibited:
    :ivar el_dtime_etrequired:
    :ivar el_dtime_etoptional:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v01"

    el_dtime_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elDTimeType",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    el_dtime_etprohibited: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elDTimeETProhibited",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            explicit_timezone="prohibited"
        )
    )
    el_dtime_etrequired: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elDTimeETRequired",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            explicit_timezone="required"
        )
    )
    el_dtime_etoptional: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elDTimeETOptional",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            explicit_timezone="optional"
        )
    )
