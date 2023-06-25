from output.models.ms_data.additional.test76423_xsd.test76423 import ClassType
from output.models.ms_data.additional.test76423_xsd.test76423 import EventType
from output.models.ms_data.additional.test76423_xsd.test76423 import EventsType
from output.models.ms_data.additional.test76423_xsd.test76423 import Jsml
from output.models.ms_data.additional.test76423_xsd.test76423 import PropertyType
from output.models.ms_data.additional.test76423_xsd.test76423 import ScopeType


obj = Jsml(
    class_value=[
        ClassType(
            events=EventsType(
                event=[
                    EventType(
                        desc="&#10;&#9;&#9;&#9;&#9;&#9;Fired when the singleton instance is created.&#10;&#9;&#9;&#9;&#9;",
                        name="InstanceCreated",
                        scope=ScopeType.CLASS
                    ),
                ]
            ),
            property=[
                PropertyType(
                    desc="&#10;&#9;&#9;&#9;&#9;Singleton instance, initialized on first access.&#10;&#9;&#9;&#9;",
                    name="instance",
                    scope=ScopeType.CLASS,
                    type_value="Singleton"
                ),
            ],
            name="Singleton"
        ),
    ]
)
