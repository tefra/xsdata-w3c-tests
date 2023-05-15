from output.models.ms_data.particles.particles_ob003_xsd.particles_ob003 import Doc
from output.models.ms_data.particles.particles_ob003_xsd.particles_ob003 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        any_element=[
            AnyElement(
                qname="{http://other}other",
                text=""
            ),
            AnyElement(
                qname="{http://other}other",
                text=""
            ),
            AnyElement(
                qname="{http://other}other",
                text=""
            ),
            AnyElement(
                qname="{http://other}other",
                text=""
            ),
        ]
    )
)
