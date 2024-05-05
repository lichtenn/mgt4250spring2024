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
Lastly, the visualization of k-means clustering helps to visualize the different groups in the sample based on BMI, Age, and Charges. In this way, it helps to understand which groups of people have similar charges and by which factors their belonging to a group of low, medium, or high cost can be explained. The visualization can help to tailor advisory services for certain patients belonging to a certain cluster. A client in cluster 1 may have to be treated differently from a client in cluster 4. In line with the results from our radar chart, the group with the highest charges is, for example, characterized by a high age and BMI. The correlation of age/BMI and charges holds true for all other clusters except the two clusters with the lowest expenses. In conclusion, the cluster is supposed to further emphasize the impact of age and BMI on medical charges

## Discussion & Summary
To incorporate existing research, 3 articles regarding medical insurance cost and the predicting factors have been considered in this project. 
* [Article on Impact of BMI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10394178/#:~:text=Studies%20have%20found%20that%20health,to%20be%20nearly%20%24114%20billion.)
* [Article on Impact of Age](https://www.healthsystemtracker.org/brief/the-burden-of-medical-debt-in-the-united-states/#:~:text=People%20typically%20use%20more%20health,adults%20to%20have%20medical%20debt.)
* [Article on Impact of Smoking Status](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6661572/#:~:text=Former%20smokers%20had%20the%20highest%20annual%20medical%20expenses%2C%20US%245590,for%20Current%20and%20Former%20smokers.)

**Findings of BMI Study:** 
A study in the United States found that adults with obesity faced significantly higher annual medical care costs, increasing with the severity of obesity, with costs doubling compared to those with normal weight. These increased costs were evident across all categories of care and were particularly pronounced for individuals covered by public health insurance programs. In 2016, the total medical cost attributable to obesity among adults in the US reached $260.6 billion, with substantial variation observed between states.

**Findings of Age Study:**
This study found a significantly positive correlation between age and medical cost. As people age, their healthcare needs and expenses tend to increase, leading to higher out-of-pocket costs. Consequently, the proportion of adults with medical debt rises with age, with middle-aged adults more likely to have medical debt compared to younger adults.

**Findings of Smoking Study:**
American adults spent an average of $4,830 annually on medical expenses. Former smokers had the highest expenditures ($5,590), followed by current smokers ($5,244), and never smokers ($4,360), with no significant difference between current and former smokers. These trends persisted across all age groups and were unaffected by years since quitting smoking. Therefore, a significant connection between smoking status and healthcare cost could be found.

### Asking AI (ChatGPT-3) - What are the determining demographic factors of medical insurance cost? 

**BMI (Body Mass Index):** This can have a significant influence, especially for conditions related to weight such as diabetes, heart disease, and joint problems. Higher BMI often correlates with higher medical costs due to increased risk of these health issues.

**Smoking (Yes/No):** Smoking can lead to various health complications such as lung disease, cancer, and heart disease, which can result in higher medical expenses. Thus, being a smoker is likely to increase medical bills.

**Age:** Age can also play a significant role. Older individuals tend to have more health issues and may require more frequent medical care, leading to higher medical bills compared to younger individuals.

**Sex:** While there may be some differences in healthcare needs between sexes, the impact on medical bills might not be as pronounced compared to other factors like BMI or smoking status. However, factors like reproductive health and preventive care might vary.
**Region:** Healthcare costs can vary significantly depending on the region due to differences in healthcare infrastructure, cost of living, availability of healthcare services, and insurance coverage. For example, medical bills might be higher in regions with higher costs of living or where healthcare services are more expensive.

**Number of Children:** This factor might not have as strong an influence on individual medical bills compared to others listed. However, it could affect overall healthcare costs for a family, especially if children require frequent medical care or specialized treatments.
Overall, while all factors listed can influence medical bills to some extent, BMI, smoking status, age, and region are likely to have the highest influence, with BMI and smoking potentially being the most significant determinants.

### Conclusion

The used AI model and the cited studies mostly confirm the results of the conducted analysis in this project. Smoking status, age, and Body Mass Index (BMI) are the top predictors for health care cost, whereas number of children, region, or sex does not play a significant role in estimating the health care expenses. Reasons for the irrelevance of the "region"-factor and this deviance from the used AI model response may be due to the large size of the different region categories. Although there are some trends regarding socioeconomic status in southwest vs. northwest United States, the differences among the regions are not as big as between different city parts in the US. The smaller the selected region, the more significant the results will be regarding that factor.


## Bibliography
Berdahl, T. A., Friedman, A. B., McCormick, D., Gourevitch, R. A., & Ballard, D. W. (2019). A new look at the 2019 health insurance coverage trends. Health Affairs, 38(10), 1612-1620.
Centers for Medicare & Medicaid Services. (2021). National Health Expenditure Data. [https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/NationalHealthExpendData]

Cawley, J., Biener, A., Meyerhoefer, C., Ding, Y., Zvenyach, T., Smolarz, B. G., & Ramasamy, A. (2021). Direct medical costs of obesity in the United States and the most populous states. Journal of managed care & specialty pharmacy, 27(3), 354–366. https://doi.org/10.18553/jmcp.2021.20410

Cutler, D. M., & Ly, D. P. (2018). The (paper) work of medicine: Understanding international medical costs. Journal of Economic Perspectives, 32(3), 3-26.

Dieleman, J. L., Baral, R., Birger, M., Bui, A. L., Bulchis, A., Chapin, A., ... & Murray, C. J. (2016). US spending on personal health care and public health, 1996-2013. JAMA, 316(24), 2627-2646.

Friedman, A. B., Gourevitch, R., Lipitz-Snyderman, A., Rahman, M., & Ballard, D. W. (2020). Trends in emergency department use by rural and urban populations in the United States. JAMA Network Open, 3(11), e2022004-e2022004.

Lassman, D., Hartman, M., Washington, B., Andrews, K., Catlin, A., & Heffler, S. (2019). US health spending trends by age and gender: Selected years 2002-10. Health Affairs, 38(2), 101-106.
Papanicolas, I., Woskie, L. R., & Jha, A. K. (2018). Health care spending in the United States and other high-income countries. JAMA, 319(10), 1024-1039.

Rakshit, S., Rakshit, S., Twitter, M. R., Claxton, G., Amin, K., & Twitter, C. C. (2024, February 12). The burden of medical debt in the United States. Peterson-KFF Health System Tracker. https://www.healthsystemtracker.org/brief/the-burden-of-medical-debt-in-the-united-states/#Share%20of%20adults%20who%20have%20medical%20debt,%20by%20health%20status%20and%20disability%20status,%202021 

Swedler, D. I., Miller, T. R., Ali, B., Waeher, G., & Bernstein, S. L. (2019). National medical expenditures by smoking status in American adults: an application of Manning's two-stage model to nationally representative data. BMJ open, 9(7), e026592. https://doi.org/10.1136/bmjopen-2018-026592
