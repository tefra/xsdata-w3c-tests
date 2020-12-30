from dataclasses import dataclass, field
from datetime import time, timedelta, timezone
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_3_9_v01"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_3_9_v01"

    el_time1: List[time] = field(
        default_factory=list,
        metadata={
            "name": "elTime1",
            "type": "Element",
            "namespace": "",
            "min_inclusive": time(8, 0, tzinfo=timezone(timedelta(seconds=36000))),
        }
    )
    el_time2: List[time] = field(
        default_factory=list,
        metadata={
            "name": "elTime2",
            "type": "Element",
            "namespace": "",
            "min_inclusive": time(0, 0, tzinfo=timezone(timedelta(seconds=3600))),
        }
    )
    el_time3: List[time] = field(
        default_factory=list,
        metadata={
            "name": "elTime3",
            "type": "Element",
            "namespace": "",
            "min_inclusive": time(10, 0, tzinfo=timezone(timedelta(seconds=46800))),
        }
    )
    el_time4: List[time] = field(
        default_factory=list,
        metadata={
            "name": "elTime4",
            "type": "Element",
            "namespace": "",
            "min_inclusive": time(3, 0, tzinfo=timezone(timedelta(seconds=14400))),
        }
    )
