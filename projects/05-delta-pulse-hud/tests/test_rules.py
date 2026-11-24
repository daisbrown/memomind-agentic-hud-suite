import pytest
from confluence_engine import from_yaml

def test_yaml_rules(tmp_path):
    pytest.importorskip('yaml')
    p = tmp_path / 'rules.yaml'; p.write_text('min_vol_oi_ratio: 4\ndelta_range: [0.3, 0.4]\n')
    assert from_yaml(p).min_ratio == 4
    p.write_text('delta_range: [0.8, 0.2]\n')
    with pytest.raises(ValueError): from_yaml(p)
