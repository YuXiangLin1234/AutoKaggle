import sys
import os
sys.path.extend(['.', '..', '../..', '../../..', '../../../..', 'multi_agents', 'multi_agents/tools', 'multi_agents/prompts'])
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tools.ml_tools import *

def generated_code_function():
    import numpy as np
    import pandas as pd
    
    import pandas as pd
    
    # Load the data
    train_path = '/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/obesity_risks/train.csv'
    test_path = '/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/obesity_risks/test.csv'
    
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    
    # Define numerical and categorical features
    numerical_features = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']
    categorical_features = ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS']
    
    # Fill missing values in numerical features
    train_df = fill_missing_values(train_df, numerical_features, method='mean')
    test_df = fill_missing_values(test_df, numerical_features, method='mean')
    
    # Fill missing values in categorical features
    train_df = fill_missing_values(train_df, categorical_features, method='mode')
    test_df = fill_missing_values(test_df, categorical_features, method='mode')
    
    
    # Handle outliers in numerical features using IQR method
    train_df = detect_and_handle_outliers_iqr(train_df, numerical_features, factor=1.5, method='clip')
    test_df = detect_and_handle_outliers_iqr(test_df, numerical_features, factor=1.5, method='clip')
    
    
    # Convert categorical features to lowercase
    for feature in categorical_features:
        train_df[feature] = train_df[feature].str.lower()
        test_df[feature] = test_df[feature].str.lower()
    
    # Convert data types for numerical features and 'id' column
    train_df = convert_data_types(train_df, numerical_features, target_type='float')
    test_df = convert_data_types(test_df, numerical_features, target_type='float')
    
    train_df = convert_data_types(train_df, 'id', target_type='int')
    test_df = convert_data_types(test_df, 'id', target_type='int')
    
    
    # Remove duplicates from the dataset
    train_df = remove_duplicates(train_df, keep='first')
    test_df = remove_duplicates(test_df, keep='first')
    
    
    # Save the cleaned datasets
    cleaned_train_path = '/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/obesity_risks/cleaned_train.csv'
    cleaned_test_path = '/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/obesity_risks/cleaned_test.csv'
    
    train_df.to_csv(cleaned_train_path, index=False)
    test_df.to_csv(cleaned_test_path, index=False)
    


    
    import pandas as pd
    import numpy as np
    
    # Load the cleaned datasets
    train_df = pd.read_csv('/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/obesity_risks/cleaned_train.csv')
    test_df = pd.read_csv('/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/obesity_risks/cleaned_test.csv')
    
    # Make copies of the dataframes
    train_df = train_df.copy()
    test_df = test_df.copy()
    
    # Create BMI feature
    train_df['BMI'] = train_df['Weight'] / (train_df['Height'] ** 2)
    test_df['BMI'] = test_df['Weight'] / (test_df['Height'] ** 2)
    
    # Categorize Age
    bins = [0, 18, 35, 50, 65, np.inf]
    labels = ['Youth', 'Young_Adult', 'Middle_Aged', 'Senior', 'Elderly']
    train_df['Age_Category'] = pd.cut(train_df['Age'], bins=bins, labels=labels)
    test_df['Age_Category'] = pd.cut(test_df['Age'], bins=bins, labels=labels)
    
    # Create Interaction Feature
    train_df['FAF_TUE_Interaction'] = train_df['FAF'] * train_df['TUE']
    test_df['FAF_TUE_Interaction'] = test_df['FAF'] * test_df['TUE']
    
    print("New features added to train_df:\n", train_df[['BMI', 'Age_Category', 'FAF_TUE_Interaction']].head())
    print("New features added to test_df:\n", test_df[['BMI', 'Age_Category', 'FAF_TUE_Interaction']].head())
    
    # Binning FCVC
    fcvc_bins = [0, 1, 2, 3, np.inf]
    fcvc_labels = ['Low', 'Medium', 'High', 'Very_High']
    train_df['FCVC_Category'] = pd.cut(train_df['FCVC'], bins=fcvc_bins, labels=fcvc_labels)
    test_df['FCVC_Category'] = pd.cut(test_df['FCVC'], bins=fcvc_bins, labels=fcvc_labels)
    
    # Binning NCP
    ncp_bins = [0, 1, 2, 3, 4, np.inf]
    ncp_labels = ['Very_Low', 'Low', 'Medium', 'High', 'Very_High']
    train_df['NCP_Category'] = pd.cut(train_df['NCP'], bins=ncp_bins, labels=ncp_labels)
    test_df['NCP_Category'] = pd.cut(test_df['NCP'], bins=ncp_bins, labels=ncp_labels)
    
    print("Transformed features added to train_df:\n", train_df[['FCVC_Category', 'NCP_Category']].head())
    print("Transformed features added to test_df:\n", test_df[['FCVC_Category', 'NCP_Category']].head())
    
    import pandas as pd
    
    # Combine train and test data to ensure consistent one-hot encoding
    train_df['is_train'] = True
    test_df['is_train'] = False
    combined_df = pd.concat([train_df, test_df])
    
    # One-hot encoding using the provided tool
    one_hot_features = ['Gender', 'CAEC', 'CALC', 'MTRANS']
    combined_df = one_hot_encode(combined_df, columns=one_hot_features, handle_unknown='ignore')
    
    # Split the combined dataframe back into train and test sets
    train_df = combined_df[combined_df['is_train']].drop(columns=['is_train'])
    test_df = combined_df[combined_df['is_train'] == False].drop(columns=['is_train', 'NObeyesdad'])
    
    # Label encoding using the provided tool
    label_features = ['family_history_with_overweight', 'FAVC', 'SMOKE', 'SCC']
    train_df = label_encode(train_df, columns=label_features)
    test_df = label_encode(test_df, columns=label_features)
    
    print("One-hot encoded features added to train_df:\n", train_df.head())
    print("One-hot encoded features added to test_df:\n", test_df.head())
    print("Label encoded features added to train_df:\n", train_df.head())
    print("Label encoded features added to test_df:\n", test_df.head())
    
    # Standard scaling using the provided tool
    numerical_features = ['Age', 'Height', 'Weight', 'BMI', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']
    train_df = scale_features(train_df, columns=numerical_features, method='standard')
    test_df = scale_features(test_df, columns=numerical_features, method='standard')
    
    print("Scaled numerical features in train_df:\n", train_df[numerical_features].head())
    print("Scaled numerical features in test_df:\n", test_df[numerical_features].head())
    
    # Save the processed datasets
    train_df.to_csv('/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/obesity_risks/processed_train.csv', index=False)
    test_df.to_csv('/mnt/d/PythonProjects/AutoKaggleMaster/multi_agents/competition/obesity_risks/processed_test.csv', index=False)
    
    print("Processed data saved successfully.")
    


if __name__ == "__main__":
    generated_code_function()