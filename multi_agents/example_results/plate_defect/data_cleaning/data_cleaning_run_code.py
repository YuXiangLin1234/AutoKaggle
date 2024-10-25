import sys
import os
sys.path.extend(['.', '..', '../..', '../../..', '../../../..', 'multi_agents', 'multi_agents/tools', 'multi_agents/prompts'])
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tools.ml_tools import *

def generated_code_function():
    import numpy as np
    import pandas as pd
    
    import pandas as pd
    
    # Load data
    train_path = '/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/plate_defect/train.csv'
    test_path = '/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/plate_defect/test.csv'
    
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    
    # Print missing values count before handling
    print("Missing values in train dataset:")
    print(train_df.isnull().sum())
    print("Missing values in test dataset:")
    print(test_df.isnull().sum())
    
    # Define columns
    numerical_columns = [
        'X_Minimum', 'X_Maximum', 'Y_Minimum', 'Y_Maximum', 'Pixels_Areas',
        'X_Perimeter', 'Y_Perimeter', 'Sum_of_Luminosity', 'Minimum_of_Luminosity', 
        'Maximum_of_Luminosity', 'Length_of_Conveyer', 'Steel_Plate_Thickness',
        'Edges_Index', 'Empty_Index', 'Square_Index', 'Outside_X_Index', 
        'Edges_X_Index', 'Edges_Y_Index', 'Outside_Global_Index', 'LogOfAreas', 
        'Log_X_Index', 'Log_Y_Index', 'Orientation_Index', 'Luminosity_Index',
        'SigmoidOfAreas'
    ]
    categorical_columns = ['TypeOfSteel_A300', 'TypeOfSteel_A400']
    
    # Fill missing values
    fill_missing_values(train_df, columns=numerical_columns, method='mean')
    fill_missing_values(train_df, columns=categorical_columns, method='mode')
    fill_missing_values(test_df, columns=numerical_columns, method='mean')
    fill_missing_values(test_df, columns=categorical_columns, method='mode')
    
    # Print missing values count after handling
    print("Missing values in train dataset after filling:")
    print(train_df.isnull().sum())
    print("Missing values in test dataset after filling:")
    print(test_df.isnull().sum())
    
    
    # List of numerical features to treat for outliers
    numerical_features = [
        'Steel_Plate_Thickness', 'Maximum_of_Luminosity', 'Minimum_of_Luminosity', 
        'X_Minimum', 'X_Maximum', 'Y_Minimum', 'Y_Maximum', 'Pixels_Areas', 
        'X_Perimeter', 'Y_Perimeter', 'Sum_of_Luminosity', 'Length_of_Conveyer', 
        'Edges_Index', 'Empty_Index', 'Square_Index', 'Outside_X_Index', 
        'Edges_X_Index', 'Edges_Y_Index', 'Outside_Global_Index', 'LogOfAreas', 
        'Log_X_Index', 'Log_Y_Index', 'Orientation_Index', 'Luminosity_Index', 
        'SigmoidOfAreas'
    ]
    
    # Handle outliers in train and test datasets
    detect_and_handle_outliers_iqr(train_df, columns=numerical_features, factor=1.5, method='clip')
    detect_and_handle_outliers_iqr(test_df, columns=numerical_features, factor=1.5, method='clip')
    
    # Print summary of outliers handled
    print("Outliers handled in train dataset.")
    print("Outliers handled in test dataset.")
    
    
    # Ensure correct data types (converting categorical to bool)
    convert_data_types(train_df, columns=categorical_columns, target_type='bool')
    convert_data_types(test_df, columns=categorical_columns, target_type='bool')
    
    # Removing duplicates
    remove_duplicates(train_df, inplace=True)
    remove_duplicates(test_df, inplace=True)
    
    # Print confirmation
    print("Data types after conversion:")
    print(train_df.dtypes)
    print(test_df.dtypes)
    print("Number of duplicate rows removed in train dataset:", len(train_df) - len(train_df.drop_duplicates()))
    print("Number of duplicate rows removed in test dataset:", len(test_df) - len(test_df.drop_duplicates()))
    
    
    # Save cleaned datasets
    cleaned_train_path = '/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/plate_defect/cleaned_train.csv'
    cleaned_test_path = '/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/plate_defect/cleaned_test.csv'
    
    train_df.to_csv(cleaned_train_path, index=False)
    test_df.to_csv(cleaned_test_path, index=False)
    
    # Print summary statistics and data types
    print("Summary statistics of cleaned train dataset:")
    print(train_df.describe())
    print("Data types of cleaned train dataset:")
    print(train_df.dtypes)
    
    print("Summary statistics of cleaned test dataset:")
    print(test_df.describe())
    print("Data types of cleaned test dataset:")
    print(test_df.dtypes)
    


if __name__ == "__main__":
    generated_code_function()