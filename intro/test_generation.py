from pathlib import Path
import duckdb

from duckdb_generate import main as generate_data_duckdb
from pandas_generate import main as generate_data_pandas
from polars_generate import main as generate_data_polars

NUM_PERSONS = 1_000_000
NUM_POSITIONS = 10_000_000
INPUT_FILE = Path(__file__).resolve().parents[1] / "data" / "companies_sorted.parquet"
CONNECTION = duckdb.connect()


def test_duckdb_generate():
    result = generate_data_duckdb(CONNECTION, INPUT_FILE, NUM_PERSONS, NUM_POSITIONS, 0)
    assert result.shape[0] == NUM_POSITIONS
    assert result.shape[1] == 5


def test_polars_generate():
    result = generate_data_polars(INPUT_FILE, NUM_PERSONS, NUM_POSITIONS, 0)
    assert result.shape[0] == NUM_POSITIONS
    assert result.shape[1] == 5


def test_pandas_generate():
    result = generate_data_pandas(INPUT_FILE, NUM_PERSONS, NUM_POSITIONS, 0)
    assert result.shape[0] == NUM_POSITIONS
    assert result.shape[1] == 5