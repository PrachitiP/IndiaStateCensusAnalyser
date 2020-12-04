import pandas as pd
from com.bridgelabz.CensusAnalyser.CensusAnalyserError import CensusAnalyserError
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianCensus
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianStateCode

class CSVLoader:
    def __init__(self, path):
        self.path = path

    def record_counter(self):
        """
        Count record in file
        :return: number of records in file
        """
        try:
            col_names = repr(IndianCensus()).split(",")
            #data = pd.read_csv(self.path)
            data = pd.read_csv(self.path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name"

    def load_State_Code(self):

        try:
            col_names = repr(IndianStateCode()).split(",")

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
    len1 = x.load_State_Code()
    print(len1)
