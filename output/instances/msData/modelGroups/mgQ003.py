from output.models.ms_data.model_groups.mg_q003_xsd.mg_q003 import Doc
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    e1_or_e2=[
        "yo",
        DerivedElement(
            qname="e2",
            value="eh?",
            type=None
        ),
        "YO!",
    ]
)
