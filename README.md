# MGT 4250 Spring 2024 Course Project
Authors: Nina Lichtenberger (nlichtenberger@elon.edu), David Neufang (dneufang@elon.edu)

## Project Description
This repository is for the final class project of MGT 4250: Data Visualization and Storytelling at Elon University. The project aimed at deploying three visualizations via Python to answer a research question. The visualizations were deployed via Streamlit Cloud and can be accessed through this [link](https://mgt4250spring2024-finalproject-lichtenberger-neufang.streamlit.app/).

### Question of Interest
The question of interest is which are the main factors determining the medical expenses of an individual in the US. More specifically, the region of residence, sex, smoker status, BMI, age, and number of children will be considered as possible influences.

### Importance
Over the last few decades, medical expenses have witnessed a significant upward trajectory, outpacing inflation rates and posing substantial financial burdens on individuals and healthcare systems globally (Dieleman et al., 2016). Studies have shown that factors such as technological advancements, increasing prevalence of chronic diseases, demographic shifts, and healthcare market dynamics contribute to the escalating costs (Lassman et al., 2019). For example, between 1996 and 2019, total national health expenditures grew from $1.4 trillion to $3.8 trillion, representing an average annual growth rate of 4.5% (Centers for Medicare & Medicaid Services, 2021).
Understanding the multitude of factors that influence medical expenses is paramount for multiple stakeholders, including policymakers, healthcare providers, insurers, and individuals themselves. For policymakers, insights garnered from this project can inform evidence-based healthcare policies, aiding in the development of targeted interventions to mitigate rising medical costs and ensure equitable access to healthcare services (Cutler et al., 2018). Healthcare providers stand to benefit from understanding the cost drivers, enabling them to optimize resource allocation and enhance cost-effective care delivery strategies (Papanicolas et al., 2018). Insurers can utilize the findings to refine risk assessment models, design tailored insurance plans, and optimize pricing structures to better serve their clients (Berdahl et al., 2019). Lastly, individuals can make more informed decisions regarding their healthcare utilization and financial planning, thereby empowering them to navigate the complex landscape of healthcare expenditures more effectively (Friedman et al., 2020).

## Data Description
### Data Source
The dataset, which served as the basis for our visualizations, can be accessed via [Kaggle](https://www.kaggle.com/datasets/rahulvyasm/medical-insurance-cost-prediction). The data is clean and was not preprocessed in any way. It was only normalized for building a regression and clustering model.

### Data Dictionary
| Column Name | Explanation                                                   |
|-------------|---------------------------------------------------------------|
| age         | Age of the observed patient                                    |
| sex         | Biological Gender of the observed patient                      |
| bmi         | Body Mass Index of the observed patient (BMI = weight in kg / (height in meters^2) ) |
| children    | Number of children of the observed patient                     |
| smoker      | Is the patient smoking cigarettes (no/yes)                     |
| region      | Current home region of the patient (northeast, northwest, southwest, southeast) |
| charges     | Annual Dollar Amount of Patient’s Insurance Charges            |

### Data Overview
The descriptive statistics show that the dataset is balanced and representative. For example, the sex as well as regions are equally distributed. Approximately 25% of the studied individuals were smokers. The age ranges from 18 to 64, meaning that we will only analyze adults. The BMI shows that the average individual in the study was overweight. Given the high number of overweight people in the US, this does not inhibit the fitness of our results for the US healthcare market, but indicates that the results may not be generalized to other countries without further robustness checks. The number of children ranges from one to 5 and the yearly charges from $1,000 to $64,000. The high discrepancy in charges highlights the importance of our research.

Descriptive Statistics for Numerical Variables:
![image](https://github.com/lichtenn/mgt4250spring2024/assets/158494941/c9559a93-d2b5-4f3e-8ddd-7c6a83be68fa)

Descriptive Statistics for Categorical Variables:
![image](https://github.com/lichtenn/mgt4250spring2024/assets/158494941/16de1e26-d3e3-4207-93d5-70bca9c89a9c)

## Interpreting Visualizations
### Average Charges by Region (Filled Map)
![image](https://github.com/lichtenn/mgt4250spring2024/assets/158494941/a391a36e-96af-482c-81d0-bbd23eb57e60)
The filled map visualization of average medical expenses across distinct regions within the US offers a comprehensive snapshot of the geographical distribution of healthcare costs. By employing a sequential color map, the visualization illustrates variations in expense levels, with darker shades indicating lower average expenses and lighter shades representing higher costs. This visual representation enables stakeholders to swiftly discern regional disparities in healthcare expenditure, a critical aspect for devising targeted interventions, risk assessments, and policies aimed at addressing the diverse needs of different communities. We can see that the states in the southeast have by far the highest average expenses with $14.500. They are followed by northeast states with an average of $13.500. Therefore, insurance companies should consider adding a premium for these states as well as offering lower rates to residents of the west. On a state level, healthcare issues are of special importance in the east and should be addressed accordingly by government stakeholders.

### Impact of Different Factors (Radar Chart)
![image](https://github.com/lichtenn/mgt4250spring2024/assets/158494941/541a4bd3-012d-42a0-a2b2-2c0de6ca4359)
The radar chart depicts the coefficients of a linear regression model. It shows the influence of different factors on the medical expenses of the individuals in the study. In this way, it helps display which factors have the highest impact. For example, it explains that being a smoker correlates strongly positively with the amount of insurance cost - BMI and Age demonstrate the same tendency and have a negative impact on the patients’ health cost. Therefore, it helps companies and policymakers to determine which group of people has the highest insurance cost and which of their features are most likely the reason for it. We can also see that the Region, Sex, and Number of Children do not have to be prioritized as highly as Smoker-Status, BMI, and Age in the risk assessment. On a government level, the plot demonstrates how critical it is to promote non-smoking as well as a healthy diet.

### Clusters of Patients
![image](https://github.com/lichtenn/mgt4250spring2024/assets/158494941/c8397ff2-2b4b-4b3b-8637-5ec5edc3d1e3)
Lastly, the visualization of k-means clustering helps to visualize the different groups in the sample based on BMI, Age, and Charges. In this way, it helps to understand which groups of people have similar charges and by which factors their belonging to a group of low, medium, or high cost can be explained. The visualization can help to tailor advisory services for certain patients belonging to a certain cluster. A client in cluster 1 may have to be treated differently from a client in cluster 4. In line with the results from our radar chart, the group with the highest charges is, for example, characterized by a high age and BMI. 

## Discussion & Summary
```python
import pandas as pd
```

## Bibliography
Berdahl, T. A., Friedman, A. B., McCormick, D., Gourevitch, R. A., & Ballard, D. W. (2019). A new look at the 2019 health insurance coverage trends. Health Affairs, 38(10), 1612-1620.
Centers for Medicare & Medicaid Services. (2021). National Health Expenditure Data. [https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/NationalHealthExpendData]

Cutler, D. M., & Ly, D. P. (2018). The (paper) work of medicine: Understanding international medical costs. Journal of Economic Perspectives, 32(3), 3-26.

Dieleman, J. L., Baral, R., Birger, M., Bui, A. L., Bulchis, A., Chapin, A., ... & Murray, C. J. (2016). US spending on personal health care and public health, 1996-2013. JAMA, 316(24), 2627-2646.

Friedman, A. B., Gourevitch, R., Lipitz-Snyderman, A., Rahman, M., & Ballard, D. W. (2020). Trends in emergency department use by rural and urban populations in the United States. JAMA Network Open, 3(11), e2022004-e2022004.

Lassman, D., Hartman, M., Washington, B., Andrews, K., Catlin, A., & Heffler, S. (2019). US health spending trends by age and gender: Selected years 2002-10. Health Affairs, 38(2), 101-106.
Papanicolas, I., Woskie, L. R., & Jha, A. K. (2018). Health care spending in the United States and other high-income countries. JAMA, 319(10), 1024-1039.

[Elon University](https://elon.edu)
![image](https://github.com/lichtenn/mgt4250spring2024/assets/158494941/382ae03b-b20a-421e-9d31-e5cf067c65ca)
