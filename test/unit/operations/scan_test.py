import pytest
from unittest.mock import patch
from unittest.mock import MagicMock

from test.utils.assertions import assertIsOperation, assertObjectsEqual, assertIsResponse
from test.utils.mocks import (
    mock_bad_gateway_exc,
    mock_table_does_not_exist_exc,
    mock_unknown_exc,
    mock_dynamo_client
)

from dynofunc.core import exceptions

from dynofunc.attribute import attr, cand, cor
from dynofunc.operations.scan import scan, run

def test_scan_is_operation():
    res = scan(table_name='users')
    assertIsOperation(res)

def test_scan_builds_basic_description():
    result = scan(table_name='users')
    expected = {
        'TableName': 'users'
    }
    assertObjectsEqual(result.description, expected)

def test_run_scan_success():
    res = run(mock_dynamo_client, {})
    assertIsResponse(res)
