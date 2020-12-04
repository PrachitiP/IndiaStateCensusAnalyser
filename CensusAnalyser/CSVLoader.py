import pandas as pd
from com.bridgelabz.CensusAnalyser.CensusAnalyserError import CensusAnalyserError
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianCensus
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianStateCode
from com.bridgelabz.CensusAnalyser.IndiaStateCode import StateCensusAnalyzer

class CSVLoader:
    def __init__(self, path, obj):
        self.path = path
        self.obj = obj

    def record_counter(self):
        """
        Count record in file
        :return: number of records in file
        """
        try:
            col_names = repr(self.obj).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")

if __name__ == "__main__":

    x  = CSVLoader(path="C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCensusData.csv")
    length = x.record_counter()
    print(length)
    CSV = CSVLoader(path="C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCensusData.csv", obj=IndianCensus())
    print(CSV.record_counter())
    CSV = CSVLoader(path="C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCode.csv",obj=StateCensusAnalyzer())
    print(CSV.record_counter())