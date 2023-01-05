"""See https://github.com/dcmi/dctap-python/issues/18#issue-1274937034 ."""

import os
from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
from dctap.config import get_config
from dctap.csvreader import csvreader, _get_rows
from dctap.defaults import CONFIGYAML, CONFIGFILE

ISSUE18_CONFIGYAML = """### dctap configuration file (in YAML format)
extra_statement_template_elements:
- severity

element_aliases:
     "Mand": "mandatory"
     "Rep": "repeatable"
"""

@pytest.mark.skip
def test_get_config_from_issue18_yamldoc(tmp_path):
    """Get config dict when passed Issue 18 YAML."""
    os.chdir(tmp_path)
    Path(CONFIGFILE).write_text(ISSUE18_CONFIGYAML)
    assert Path(CONFIGFILE).is_file()
    config_dict = get_config()
    assert config_dict["element_aliases"] == {"Mand": "mandatory", "Rep": "repeatable"}
    assert config_dict["extra_statement_template_elements"] == ["severity"]

def test_get_element_aliases_from_default_yamldoc(tmp_path):
    """Get config dict (with element aliases) directly from built-in defaults."""
    os.chdir(tmp_path)
    config_dict = get_config(default_configyaml_str=CONFIGYAML)
    assert config_dict["element_aliases"]["propertyid"] == "propertyID"
    assert config_dict["element_aliases"]["mandatory"] == "mandatory"
    assert config_dict["element_aliases"]["repeatable"] == "repeatable"