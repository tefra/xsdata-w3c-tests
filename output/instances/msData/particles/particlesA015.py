from output.models.ms_data.particles.particles_a015_xsd.particles_a015 import Doc
from output.models.ms_data.particles.particles_a015_xsd.particles_a015 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        any_element=[
            AnyElement(
                qname='{foo}any',
                text='\n\t\t\ttesting\n\t\t'
            ),
            AnyElement(
                qname='{foo}foo',
                text='\n\t\t\treally testing\n\t\t'
            ),
            AnyElement(
                qname='{foo}foo',
                text='\n\t\t\treally testing\n\t\t'
            ),
        ]
    )
)
