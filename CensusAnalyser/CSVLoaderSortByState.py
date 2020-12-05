import pandas as pd
from com.bridgelabz.CensusAnalyser.CensusAnalyserError import CensusAnalyserError
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianCensus
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianStateCode
from com.bridgelabz.CensusAnalyser.IndiaStateCode import StateCensusAnalyzer

# class CSVLoader:
#     def __init__(self, path):
#         self.path = path
#
#
#     def record_counter(path):
#         """
#         Count record in file
#         :return: number of records in file
#         """
#         try:
#             census_col_names = repr(IndianCensus()).split(",")
#             data = pd.read_csv(path, usecols=census_col_names)
#             return data
#         except FileNotFoundError:
#             raise CensusAnalyserError("Check file path")
#         except ValueError:
#             raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")
#
#     def load_State_Code(path):
#
#         try:
#             state_col_names = repr(IndianStateCode()).split(",")
#             data = pd.read_csv(path, usecols=state_col_names)
#             return data
#
#         except FileNotFoundError:
#             raise CensusAnalyserError("Check file path")
#         except ValueError:
#             raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")
#
#
# if __name__ == "__main__":
#
#     x  = CSVLoader(path="C:/Users/PRACHITI PATIL/PycharmProjects/CensusAnalyzer/resources/IndiaStateCensusData.csv")
#     length = x.record_counter()
#     print(length)
#     len1 = x.load_State_Code()
#     print(len1)
class CSVLoaderS:
    def __init__(self, path):
        self.path = path

    def record_counter(path):
        """
        Count record in file
        :return: number of records in file
        """
        try:
            col_names = repr(IndianCensus()).split(",")
            #data = pd.read_csv(path)
            data = pd.read_csv(path, usecols=col_names)
            return data
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")

    def load_State_Code(path):
        try:
            col_names = repr(IndianStateCode()).split(",")
            #data = pd.read_csv(path)
            data = pd.read_csv(path, usecols=col_names)
            return data

        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")

        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")


if __name__ == "__main__":
    x  = CSVLoaderS(path="C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/IndiaStateCensusData.csv")
    length = x.record_counter()
    print(length)
    y = CSVLoaderS(path="C:/Users/PRACHITI PATIL/PycharmProjects/IndianCensusAnalysisProgram/resources/IndiaStateCode.csv")
    len1 = y.load_State_Code()
    print(len1)
