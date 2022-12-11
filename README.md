# Heart Disease Risk Analysis

## Movitation
Heart disease is the leading cause of death in the United States.  The term “heart disease” refers to several types of heart conditions. In the United States, the most common type of heart disease is coronary artery disease (CAD), which can lead to heart attack.

- What are risk factors that may cause heart disease?
- What's your risk level for heart disease? 
- How can you greatly reduce risk for heart disease through lifestyle changes and, in some cases, medicine? 

## Data Source
- The data source was from [CDC](https://data.cdc.gov/)
- The dataset was tailored and downloaded from [Kaggle](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease/download?datasetVersionNumber=2)

## Data Design
- Review and clean the data
- Explore the data to identify the key factors
- Build up the classificaiton model to predict the probability for heart disease
- Run the model to indicate the risk level
- Based the risk level, provide the meaningful information to end user(s)

## Data Exploration

- Heart disease can happen at any age, but the risk goes up as you age.

![image](https://user-images.githubusercontent.com/97680882/205699619-7ecb6949-4302-4071-8223-e96ca6af9c69.png)

- Heart disease is the number one killer of both men and women. But men's heart disease probability may be higher than women. 

![image](https://user-images.githubusercontent.com/97680882/205700701-de990356-b8e0-4c80-a3d8-b3a45ff74655.png)

- Some groups for heart disease are more likely to have conditions that increase their risk for cardiovascular disease. American native has the highest probability compared to other races. 

![image](https://user-images.githubusercontent.com/97680882/205702299-e5c08eeb-9a05-441d-bb97-7d0ca3f577fe.png)

- Body Mass Index (BMI) is a useful measure of overweight and obesity. It is calculated from the height and weight. The higher your BMI, the higher your risk for heart disease. 

![image](https://user-images.githubusercontent.com/97680882/205705530-edc5c8d7-9760-4416-8544-96c4ed81f72a.png)

## Data Model
- Dependent Variable: Heart Disease Probability
- Independent Variables: 
  - BMI
  - Smoking
  - Alcohol Drinking
  - Stroke
  - Physical Health
  - Mental Health
  - Difficult Walking
  - Sex
  - Age
  - Race
  - Diabete
  - Sports
  - General Health
  - Sleep Time
  - Asthama
  - Kidney Disease
  - Skin Cancer
- Classification Model: Logit Regression Model

## Streamlit App
Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better. Here is the published streamlit [app](https://heartdisease.streamlit.app/) for heart disease analysis. 
 
## Future Work
I plan to add more factors to imporve the accuracy of the model for the future work.  
