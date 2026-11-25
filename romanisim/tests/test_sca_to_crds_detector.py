"""Purpose: CRDS ePSF lookups use WFI## detector names, not SCA##."""

import pytest

from romanisim.psf import sca_to_crds_detector


@pytest.mark.parametrize(
    "sca, expected",
    [
        (2, "WFI02"),
        (4, "WFI04"),
        ("SCA02", "WFI02"),
        ("sca4", "WFI04"),
        ("WFI07", "WFI07"),
        ("wfi18", "WFI18"),
    ],
)
def test_sca_to_crds_detector_maps_to_wfi(sca, expected):
    assert sca_to_crds_detector(sca) == expected


def test_sca_to_crds_detector_rejects_out_of_range():
    with pytest.raises(ValueError, match="Invalid SCA"):
        sca_to_crds_detector(0)
    with pytest.raises(ValueError, match="Invalid SCA"):
        sca_to_crds_detector(19)
