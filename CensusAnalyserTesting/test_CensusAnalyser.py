from com.bridgelabz.CensusAnalyser.CSVLoader import CSVLoader
from com.bridgelabz.CensusAnalyser.CensusAnalyserError import CensusAnalyserError
import pytest

CENSUS_CSV_FILE_PATH = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCensusData.xsl"
CENSUS_CSV_FILE_WRONG_DELIMITER = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/USStateCensusData.csv"
CENSUS_CSV_WRONG_HEADER = "C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateData.csv"

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