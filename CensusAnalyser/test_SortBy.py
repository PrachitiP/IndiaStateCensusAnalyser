from com.bridgelabz.CensusAnalyser.IndianCensus import IndianStateCode
from com.bridgelabz.CensusAnalyser.IndiaStateCode import StateCensusAnalyzer
from com.bridgelabz.CensusAnalyser.CensusAnalyserSortByState import CensusAnalyserSortByState
from com.bridgelabz.CensusAnalyser.CSVLoaderSortByState import CSVLoaderS

import pytest
import json

CENSUS_CSV_FILE_PATH = "C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = "C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/IndiaStateCensusData.xsl"
CENSUS_CSV_FILE_WRONG_DELIMITER = "C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/USStateCensusData.csv"
CENSUS_CSV_WRONG_HEADER = "C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/IndiaStateData.csv"
STATE_CODE_WITH_FILE_PATH = "C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/IndiaStateCode.csv"
STATE_CODE_WITH_WRONG_PATH = "IndiaStateCode.csv"
STATE_CODE_WITH_WORNG_TYPE = "C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/IndiaStateCode.txt"
STATE_CODE_WITH_WRONG_HEADER = "C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/IndiaStateCensusData.csv"
STATE_CODE_CSV_WRONG_DELIMITER = "C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/IndiaStateCodeInvalidDelimiter.csv"

#UC3
def test_IndianCensusData_SortByState():
    census_analyser = CensusAnalyserSortByState(CENSUS_CSV_FILE_PATH)
    census_analyser.census_record_counter()
    sorted_json = census_analyser.sort_by_state()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["State"] == "Andhra Pradesh"