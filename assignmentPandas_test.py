import assignmentPandas

def testColumnNames():
    expected_cols = ['CustomerID', 
                     'Name', 
                     'City', 
                     'Age', 
                     'NumberOfPurchases',
                     'TotalPurchaseAmount']
    df = assignmentPandas.problem1("CustomerInformation.csv", 
                              "CustomerPurchaseHistory.csv")
    assert list(df.columns) == expected_cols

def testAverageAge():
    expected_avg_age = 29
    df = assignmentPandas.problem1("CustomerInformation.csv", 
                              "CustomerPurchaseHistory.csv")
    assert df["Age"].mean() == expected_avg_age

def testMaxTotalPurchaseAmount():
    expected_max_purchase = 4096
    df = assignmentPandas.problem1("CustomerInformation.csv", 
                              "CustomerPurchaseHistory.csv")
    assert df["TotalPurchaseAmount"].max() == expected_max_purchase
