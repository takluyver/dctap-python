"""Return config dictionary from reading config file."""

import os
import pytest
from pathlib import Path
from dctap.config import get_config
from dctap.csvreader import csvreader
from dctap.defaults import CONFIGFILE1
from dctap.exceptions import ConfigError


@pytest.mark.skip
def test_get_config_file_extra_aliases(tmp_path):
    """@@@@@@."""
    os.chdir(tmp_path)
    Path(CONFIGFILE1).write_text("""
    extra_element_aliases:
        "ShapID": "shapeID"
    """)
    config_dict = get_config()
    assert "extra_element_aliases" in config_dict
    assert "propertyid" in config_dict.get("element_aliases")
    assert "shapid" in config_dict.get("element_aliases")
