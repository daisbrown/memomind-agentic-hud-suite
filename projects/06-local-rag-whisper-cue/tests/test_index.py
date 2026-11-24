from local_index import LocalIndex

def test_index_ignores_empty_and_ranks(tmp_path):
    a = tmp_path / 'a.md'; b = tmp_path / 'b.md'
    a.write_text('BLE BLE retry'); b.write_text('BLE timeout')
    idx = LocalIndex([a,b])
    assert idx.search('') == []
    assert idx.search('BLE')[0][1] == str(a)
    assert idx.search('unknown') == []
