from csv_feed import read_ticks, filter_ticks
from simulate_options_tape import ConfluenceEngine

def test_csv(tmp_path):
    p=tmp_path/'ticks.csv'; p.write_text('ticker,contract,vol_oi,delta,ask,ivr,time\nNVDA,145C,4,.38,2.45,42,1\n')
    assert filter_ticks(read_ticks(p),ConfluenceEngine())[0].ticker == 'NVDA'
