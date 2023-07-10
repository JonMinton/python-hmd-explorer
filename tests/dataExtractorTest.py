import unittest

from collections import Counter

from models.dataExtractor import DataExtractor

def listsHaveSameElements(actualList, expectedList):
    countActual = Counter(actualList)
    countExpected = Counter(expectedList)

    return countActual == countExpected

class TestDataExtractor(unittest.TestCase):


    
    def setUp(self):
        self.dataExtractor = DataExtractor()

    def test_canSetBasePath(self):
        self.assertEqual(self.dataExtractor.basePath, None)
        self.dataExtractor.setBasePath("assets/data")
        self.assertEqual(self.dataExtractor.basePath, "assets/data")

    def test_canGetBasePath(self):
        self.dataExtractor.setBasePath("assets/data")
        self.assertEqual(self.dataExtractor.getBasePath(), "assets/data")

    def test_canSetFileType(self):
        self.assertEqual(self.dataExtractor.getFileType(), None)
        self.dataExtractor.setFileType("csv")
        self.assertEqual(self.dataExtractor.getFileType(), "csv")

    def test_canSearchAllFilesInBasePath(self):
        self.dataExtractor.setBasePath("tests/assets/data")


        
        self.assertFalse(
            listsHaveSameElements(
            self.dataExtractor.getAllFilesInBasePath(), 
                ["tests/assets/data/correctType.csv", 
                 "tests/assets/data/incorrectType.txt"
            ]))
        
        self.dataExtractor.searchAllFilesInBasePath()

        self.assertTrue(
            listsHaveSameElements(
            self.dataExtractor.getAllFilesInBasePath(), 
                ["tests/assets/data/correctType.csv", 
                 "tests/assets/data/incorrectType.txt"
            ]))
        
    def test_canGetAllValidFilesInBasePath(self):
        self.dataExtractor.setBasePath("tests/assets")
        self.dataExtractor.setFileType("csv")
        self.dataExtractor.searchFilesInBasePath()

        self.assertEqual(
            self.dataExtractor.getFilesInBasePath(), 
            ["tests/assets/data/correctType.csv"]
        )
        
    def test_canLoadFile(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        self.assertEqual(self.dataExtractor.getLoadedFile().shape, (1248750, 7))

    def test_canGetUniqueCountryCodesInLoadedFile(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        countryCodes = self.dataExtractor.getUniqueCountryCodesInFile()
        self.assertEqual(len(countryCodes), 41)
    
    def test_canGetUniqueCountriesInLoadedFile(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        countries = self.dataExtractor.getUniqueCountriesInFile()
        self.assertEqual(len(countries), 41)

    def test_numUniqueCountriesAndCountryCodesAreEqual(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        countryCodes = self.dataExtractor.getUniqueCountryCodesInFile()
        countries = self.dataExtractor.getUniqueCountriesInFile()
        self.assertEqual(len(countryCodes), len(countries))
        
    def test_canGetUniqueSexesInLoadedFile(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        sexes = self.dataExtractor.getUniqueSexesInFile()
        self.assertEqual(len(sexes), 3)
        self.assertTrue(listsHaveSameElements(
            sexes,
            ['male', 'female', 'total']
            )
        )

    def test_canGetUniqueAgesInFile(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        ages = self.dataExtractor.getUniqueAgesInFile()
        self.assertEqual(len(ages), 111)

    def test_canGetUniqueYearsInFile(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        years = self.dataExtractor.getUniqueYearsInFile()
        self.assertEqual(len(years), 272)

    def test_canGetDataByCountryCode(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        data = self.dataExtractor.getDataByCountryCode("CAN")
        self.assertEqual(data.shape, (33300, 7))

    def test_canGetDataByCountryCodeAndSex(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        data = self.dataExtractor.getDataByCountryCodeAndSex("CAN", "male")
        self.assertEqual(data.shape, (11100, 7))

    def test_canCheckIfCountryCodeIsValid(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        self.assertTrue(self.dataExtractor.checkIfCountryCodeIsValid("CAN"))
        self.assertFalse(self.dataExtractor.checkIfCountryCodeIsValid("ABC"))

    def test_canCheckIfSexIsValid(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        self.assertTrue(self.dataExtractor.checkIfSexIsValid("male"))
        self.assertFalse(self.dataExtractor.checkIfSexIsValid("somethingElse"))

    def test_canCheckIfAgeIsValid(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        self.assertTrue(self.dataExtractor.checkIfAgeIsValid(7))
        self.assertFalse(self.dataExtractor.checkIfAgeIsValid(-4))
        self.assertFalse(self.dataExtractor.checkIfAgeIsValid(251))

    def test_canReturnImpliedCohort(self):
        self.dataExtractor.setBasePath("assets/data")
        self.dataExtractor.loadFile("population.csv")
        selectedSex = 'male'
        selectedCountryCode = 'CAN'
        selectedAge = 7
        selectedYear = 2017
        