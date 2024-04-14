import pytest
import system_info

def test_cpu_under_60_precent():
    assert system_info.cpu_usage() < 60
