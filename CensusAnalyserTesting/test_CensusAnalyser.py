from com.bridgelabz.CensusAnalyser.CSVLoader import CSVLoader
from com.bridgelabz.CensusAnalyser.CensusAnalyserError import CensusAnalyserError
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianCensus
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianStateCode
from com.bridgelabz.CensusAnalyser.IndiaStateCode import StateCensusAnalyzer
import pytest

CENSUS_CSV_FILE_PATH = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCensusData.xsl"
CENSUS_CSV_FILE_WRONG_DELIMITER = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/USStateCensusData.csv"
CENSUS_CSV_WRONG_HEADER = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateData.csv"
STATE_CODE_WITH_FILE_PATH = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCode.csv"
STATE_CODE_WITH_WRONG_PATH = "IndiaStateCode.csv"
STATE_CODE_WITH_WORNG_TYPE = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCode.txt"
STATE_CODE_WITH_WRONG_HEADER = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCensusData.csv"
STATE_CODE_CSV_WRONG_DELIMITER = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCodeInvalidDelimiter.csv"
obj_india_census = IndianCensus()
obj_india_states = StateCensusAnalyzer()

# check if length of records is same or not
def test_record_counter():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_PATH)
    assert csv_loader.record_counter() == 29

#Check if file is incorrct and returns custom exception
def test_record_counter_wrong_file_path():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()

#Check if correct file with wrong type
def test_record_counter_wrong_file_type():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()

#Check if files is correct but delimiter is wrong
def test_record_delimiter_wrong():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()

#Check when file is correct but header is incorrect
def test_record_header_is_incorrect():
    csv_loader = CSVLoader(CENSUS_CSV_WRONG_HEADER)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()
#UC2
# check if length of records is same or not
def test_loadstatecode():
    csv_loader = CSVLoader(STATE_CODE_WITH_FILE_PATH)
    assert csv_loader.load_State_Code() == 37

#Check if file is incorrct and returns custom exception
def test_record_counter_wrong_file_path():
    csv_loader = CSVLoader(STATE_CODE_WITH_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_loader.load_State_Code()

#Check if correct file with wrong type
def test_record_counter_wrong_file_type():
    csv_loader = CSVLoader(STATE_CODE_WITH_WORNG_TYPE)
    with pytest.raises(CensusAnalyserError):
        csv_loader.load_State_Code()

#Check if files is correct but delimiter is wrong
def test_record_delimiter_wrong():
    csv_loader = CSVLoader(STATE_CODE_CSV_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        csv_loader.load_State_Code()

#Check when file is correct but header is incorrect
def test_record_header_is_incorrect():
    csv_loader = CSVLoader(STATE_CODE_WITH_WRONG_HEADER)
    with pytest.raises(CensusAnalyserError):
        csv_loader.load_State_Code()

#UC2-Refactor 1 and 2
def test_record_counter():

    csv_loader = CSVLoader(CENSUS_CSV_FILE_PATH, obj_india_census)
    assert csv_loader.record_counter() == 29


def test_record_counter_for_wrong_file_path():

    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH, obj_india_census)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_file_type():

    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE, obj_india_census)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_delimiter():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER, obj_india_census)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_header():
    csv_loader = CSVLoader(CENSUS_CSV_WRONG_HEADER , obj_india_census)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_csv_states():

    csv_states_loader = CSVLoader(STATE_CODE_WITH_FILE_PATH, obj_india_states)
    assert csv_states_loader.record_counter() == 37


def test_record_counter_for_wrong_file_path_csv_states():

    csv_states_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH, obj_india_states)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_file_type_csv_states():

    csv_states_loader = CSVLoader(STATE_CODE_WITH_WORNG_TYPE, obj_india_states)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_delimiter_csv_states():
    csv_states_loader = CSVLoader(STATE_CODE_CSV_WRONG_DELIMITER, obj_india_states)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_header_csv_states():
    csv_states_loader = CSVLoader(STATE_CODE_WITH_WRONG_HEADER, obj_india_states)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()

