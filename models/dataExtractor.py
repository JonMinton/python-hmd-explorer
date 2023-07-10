import pandas as pd
import os


class DataExtractor:

    def __init__(self, basePath = None, fileType = None):
        self.basePath = None
        self.fileType = None
        self.listOfFiles = None
        self.listOfAllFiles = None
        self.df = None
        self.dfSubset = None
        self.dfType = None
        self.uniqueSexes = None
        self.uniqueCountries = None
        self.uniqueCountryCodes = None
        self.uniqueAges = None
        self.uniqueYears = None
    

    def setFileType(self, fileType):
        self.fileType = fileType

    def getFileType(self):
        return self.fileType
    
    def setBasePath(self, basePath):
        self.basePath = basePath

    def getBasePath(self):
        return self.basePath
    
    def searchAllFilesInBasePath(self):
        self.listOfAllFiles = []
        for root, dirs, files in os.walk(self.basePath):
            for file in files:
                self.listOfAllFiles.append(os.path.join(root, file))

    def getAllFilesInBasePath(self):
        return self.listOfAllFiles
    
    def searchFilesInBasePath(self):
        self.listOfFiles = []
        for root, dirs, files in os.walk(self.basePath):
            for file in files:
                if file.endswith(self.fileType):
                    self.listOfFiles.append(os.path.join(root, file))
    
    def getFilesInBasePath(self):
        return self.listOfFiles
    
    def loadFile(self, fileName):
        self.df = pd.read_csv(os.path.join(self.basePath, fileName))

    def getLoadedFile(self):
        return self.df
    
    def getUniqueCountryCodesInFile(self):
        return self.df["cntry"].unique()

    def getUniqueCountriesInFile(self):
        return self.df["country"].unique()
    
    def getUniqueSexesInFile(self):
        return self.df["sex"].unique()
    
    def getUniqueAgesInFile(self):
        return self.df["age"].unique()
    
    def getUniqueYearsInFile(self):
        return self.df["year"].unique()
    
    def getDataByCountryCode(self, countryCode):
        return self.df.loc[self.df["cntry"] == countryCode, :]

    def setDataByCountryCodeAndSex(self, countryCode, sex):
        self.dfSubset =  self.df.loc[(self.df['cntry'] == countryCode) & (self.df['sex'] == sex),:]

    def setDataByCountryCodeAndSex(self, countryCode, sex):
        self.dfSubset =  self.df.loc[(self.df['cntry'] == countryCode) & (self.df['sex'] == sex),:]

    def checkIfCountryCodeIsValid(self, countryCode):
        return countryCode in self.getUniqueCountryCodesInFile()
    
    def checkIfSexIsValid(self, sex):
        return sex in self.getUniqueSexesInFile()
    
    def checkIfAgeIsValid(self, age):
        return age in self.getUniqueAgesInFile()
    
    def checkIfYearIsValid(self, year):
        return year in self.getUniqueYearsInFile()

    def getImpliedCohort(self, age, year):
        if self.checkIfAgeIsValid(age) and self.checkIfYearIsValid(year):
            return year - age
    
