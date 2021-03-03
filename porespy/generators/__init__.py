r"""

===============================================================================
generators
===============================================================================

**Generate Artificial Images**

This module contains a variety of functions for generating artificial images
of porous materials, generally for testing, validation, debugging, and
illustration purposes.

.. autosummary::

    porespy.generators.blobs
    porespy.generators.bundle_of_tubes
    porespy.generators.cylinders
    porespy.generators.insert_shape
    porespy.generators.lattice_spheres
    porespy.generators.line_segment
    porespy.generators.overlapping_spheres
    porespy.generators.perlin_noise
    porespy.generators.polydisperse_spheres
    porespy.generators.pseudo_gravity_packing
    porespy.generators.random_cantor_dust
    porespy.generators.RSA
    porespy.generators.sierpinski_foam
    porespy.generators.voronoi_edges

.. autofunction:: blobs
.. autofunction:: bundle_of_tubes
.. autofunction:: cylinders
.. autofunction:: cylinders_porosity
.. autofunction:: insert_shape
.. autofunction:: lattice_spheres
.. autofunction:: line_segment
.. autofunction:: overlapping_spheres
.. autofunction:: perlin_noise
.. autofunction:: polydisperse_spheres
.. autofunction:: pseudo_gravity_packing
.. autofunction:: random_cantor_dust
.. autofunction:: RSA
.. autofunction:: sierpinski_foam
.. autofunction:: voronoi_edges

"""

from .__imgen__ import blobs
from .__imgen__ import bundle_of_tubes
from .__imgen__ import cylinders
from .__imgen__ import insert_shape
from .__imgen__ import lattice_spheres
from .__imgen__ import line_segment
from .__imgen__ import overlapping_spheres
from .__imgen__ import perlin_noise
from .__imgen__ import polydisperse_spheres
from .__imgen__ import RSA
from .__imgen__ import voronoi_edges
from .__imgen__ import pseudo_gravity_packing
from .__electrostatic__ import pseudo_electrostatic_packing
from .__fractals__ import random_cantor_dust
from .__fractals__ import sierpinski_foam
from .__cylinder__ import cylindrical_plug
