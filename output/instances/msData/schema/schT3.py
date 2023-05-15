from output.models.ms_data.schema.sch_t3_a_xsd.sch_t3_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}e1",
            text="",
            attributes={
                "att1": "123",
                "att3": "123",
                "att5": "123",
                "att6": "true",
                "att7": "123",
                "att9": "123",
                "att11": "1",
                "att12": "true",
                "att13": "fix",
                "att14": "true",
                "att15": "fix",
                "att16": "fix",
            }
        ),
        AnyElement(
            qname="{ns-a}b-e1",
            text="",
            attributes={
                "att1": "123",
                "att3": "123",
                "att5": "123",
                "att6": "true",
                "att7": "123",
                "att9": "123",
                "att11": "1",
                "att12": "true",
                "att13": "fix",
                "att14": "true",
                "att15": "fix",
                "att16": "fix",
            }
        ),
        AnyElement(
            qname="{ns-a}e2",
            text="12"
        ),
    ]
)
