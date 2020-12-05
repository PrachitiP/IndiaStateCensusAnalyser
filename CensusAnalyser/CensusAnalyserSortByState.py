import pandas as pd
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianCensus
from com.bridgelabz.CensusAnalyser.CSVLoaderSortByState import CSVLoaderS
from com.bridgelabz.CensusAnalyser.IndianCensus import IndianStateCode
class CensusAnalyserSortByState:
    dataList = pd.DataFrame()

    def __init__(self, path):
        self.path = path

    def census_record_counter(self):
        CensusAnalyserSortByState.dataList = CSVLoaderS.record_counter(self.path)
        return len(CensusAnalyserSortByState.dataList)

    def state_code_record_counter(self):
        CensusAnalyserSortByState.dataList = CSVLoaderS.load_State_Code(self.path)
        return len(CensusAnalyserSortByState.dataList)

    def sort_by_state(self):
        CensusAnalyserSortByState.dataList.sort_values(by=[IndianCensus().state], inplace=True)
        return CensusAnalyserSortByState.dataList.to_json(orient='records')

    def sort_by_stateCode(self):
        CensusAnalyserSortByState.dataList.sort_values(by=[IndianStateCode().state_code], inplace=True)
        return CensusAnalyserSortByState.dataList.to_json(orient='records')