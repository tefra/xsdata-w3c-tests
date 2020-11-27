from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.vehicle.org"


@dataclass
class Person:
    class Meta:
        name = "person"
        namespace = "http://www.vehicle.org"

    car: List["Person.Car"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Car:
        reg_state: Optional[str] = field(
            default=None,
            metadata={
                "name": "regState",
                "type": "Attribute",
            }
        )
        reg_plate: Optional[int] = field(
            default=None,
            metadata={
                "name": "regPlate",
                "type": "Attribute",
            }
        )


@dataclass
class Vehicle:
    class Meta:
        name = "vehicle"
        namespace = "http://www.vehicle.org"

    plate_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "plateNumber",
            "type": "Attribute",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class State:
    class Meta:
        name = "state"
        namespace = "http://www.vehicle.org"

    code: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    person: List[Person] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.vehicle.org"

    state: List[State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
