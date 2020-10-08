from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v03"


@dataclass
class DTimeRoot:
    """
    :ivar el_dtime_et:
    :ivar el_dtime_list_required:
    :ivar el_dtime_list_prohibited:
    :ivar el_dtime_list_optional:
    """
    class Meta:
        name = "dTimeRoot"

    el_dtime_et: Optional[str] = field(
        default=None,
        metadata=dict(
            name="elDTimeET",
            type="Element",
            namespace="",
            required=True,
            explicit_timezone="required"
        )
    )
    el_dtime_list_required: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elDTimeListRequired",
            type="Element",
            namespace="http://xstest-tns/schema11_F4_3_16_v03",
            required=True,
            explicit_timezone="required",
            tokens=True
        )
    )
    el_dtime_list_prohibited: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elDTimeListProhibited",
            type="Element",
            namespace="http://xstest-tns/schema11_F4_3_16_v03",
            required=True,
            explicit_timezone="prohibited",
            tokens=True
        )
    )
    el_dtime_list_optional: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elDTimeListOptional",
            type="Element",
            namespace="http://xstest-tns/schema11_F4_3_16_v03",
            required=True,
            explicit_timezone="optional",
            tokens=True
        )
    )


@dataclass
class ElDtimeListOptional:
    """
    :ivar value:
    """
    class Meta:
        name = "elDTimeListOptional"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            explicit_timezone="optional",
            tokens=True
        )
    )


@dataclass
class ElDtimeListProhibited:
    """
    :ivar value:
    """
    class Meta:
        name = "elDTimeListProhibited"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            explicit_timezone="prohibited",
            tokens=True
        )
    )


@dataclass
class ElDtimeListRequired:
    """
    :ivar value:
    """
    class Meta:
        name = "elDTimeListRequired"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            explicit_timezone="required",
            tokens=True
        )
    )


@dataclass
class Root(DTimeRoot):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"
