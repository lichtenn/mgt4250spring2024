import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
st.title("Demographic Influences on Medical Charges")

df = pd.read_csv("medical_insurance.csv", sep=';')

col1, col2 = st.columns([5, 5])
with col1: # for figure 1
    st.header("1. Average Charges by Region")
    # Define charges per region
    charges_per_region = {
        'northeast': 13475.874737,
        'northwest': 12463.129315,
        'southeast': 14748.777706,
        'southwest': 12164.196435
    }
    
    # Define states per region
    southeast_states = [
        'AL', 'AR', 'FL', 'GA', 'KY', 'LA', 
        'MS', 'NC', 'SC', 'TN', 'VA', 'WV', 'MO'
    ]
    
    southwest_states = [
        'AZ', 'NM', 'TX', 'OK', 'CO'
    ]
    
    northwest_states = [
        'AK', 'ID', 'MT', 'OR', 'WA', 'WY',
        'NV', 'UT', 'IA', 'MN', 'NE', 'ND', 
        'SD', 'KS', 'CA'
    ]
    
    northeast_states = [
        'CT', 'DE', 'ME', 'MD', 'MA', 
        'NH', 'NJ', 'NY', 'PA', 'RI', 
        'VT', 'IL', 'IN', 'MI', 'OH', 'WI',
    ]
    
    # Create a dictionary to map states to regions
    state_to_region = {}
    for state in southeast_states:
        state_to_region[state] = 'southeast'
    for state in southwest_states:
        state_to_region[state] = 'southwest'
    for state in northwest_states:
        state_to_region[state] = 'northwest'
    for state in northeast_states:
        state_to_region[state] = 'northeast'
    
    # Create DataFrame
    data = {'State': [], 'Charges': []}
    for state, region in state_to_region.items():
        data['State'].append(state)
        data['Charges'].append(charges_per_region[region])
    
    charges_per_state = pd.DataFrame(data)
    
    fig1 = px.choropleth(locations=charges_per_state["State"],
             locationmode="USA-states", scope="usa", 
              color=charges_per_state["Charges"],
             color_continuous_scale="Viridis")
    st.plotly_chart(fig1, use_container_width=True)
    st.write("Please note that the average charges displayed per State relate to the region of State.")

with col2:
    st.header("2. Impact of Different Factors")
    dummy_columns = pd.get_dummies(df[['sex', 'region', 'smoker']], dtype = int)
    
    # Concatenating the dummy columns with the original DataFrame
    df = pd.concat([df, dummy_columns], axis=1)
    
    # Dropping the original categorical columns if needed
    df.drop(['sex', 'region', 'smoker'], axis=1, inplace=True)
    df.drop(['sex_female','region_northeast','smoker_no'], axis=1, inplace=True)
    
    # normalizing age, bmi and children
    
    from sklearn.preprocessing import MinMaxScaler
    
    # Define columns to normalize
    columns_to_normalize = ['age', 'bmi', 'children']
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the selected columns
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
    
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    
    # Define independent variables and dependent variable
    X = df[['age', 'bmi', 'children', 'region_northwest', 'region_southwest', 'region_southeast', 'smoker_yes', 'sex_male']]
    y = df['charges']
    
    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the linear regression model
    model = LinearRegression()
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Predictions on the test set
    y_pred = model.predict(X_test)
    
    coefficients = model.coef_
    features = X.columns
    
    import numpy as np
    
    # Assuming 'model' is your trained linear regression model
    coefficients = model.coef_
    
    # Define the variable names based on the coefficients
    categories = ['Age', 'BMI', 'Children', 'Region_Northeast', 'Region_Southwest', 'Region_Southeast', 'Smoker_Yes', 'Sex_Male']
    
    # Number of variables
    num_vars = len(categories)
    
    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Make the plot close to a circle
    values = coefficients.tolist()
    angles += [angles[0]]  # Add the first angle again for the dummy category
    
    # Create a DataFrame for Plotly Express
    data = {'categories': categories, 'values': values}
    coefficients_by_category = pd.DataFrame(data)
    
    # Plot
    fig2 = px.line_polar(coefficients_by_category, r='values', theta='categories', line_close=True)
    fig2.update_traces(fill='toself', line=dict(color='blue', width=2), fillcolor='skyblue', opacity=0.5)
    fig2.update_layout(polar=dict(radialaxis=dict(visible=False)), showlegend=False)
    
    st.plotly_chart(fig2, use_container_width=True)

st.header("3. Clusters of Patients")
from sklearn.cluster import KMeans
m = st.number_input("How many clusters do you want to form?", value=5)
km = KMeans(n_clusters=m, random_state=0, n_init=10) 
km = km.fit(df) 
df["Cluster"] = km.labels_
df.sort_values(by="Cluster")

# Create the 3D scatter plot
fig3 = px.scatter_3d(df, x='charges', y='age', z='bmi', color='Cluster', color_continuous_scale='viridis',
                    symbol='Cluster', opacity=0.7, size_max=5)

# Customize axis labels
fig3.update_layout(scene=dict(xaxis_title='Charges', yaxis_title='Age', zaxis_title='BMI'))

# Move the color legend to the top right corner
fig3.update_layout(legend=dict(
    orientation="h",
    yanchor="top",
    y=1.02,
    xanchor="right",
    x=1
))

# Show the plot
st.plotly_chart(fig3, use_container_width=True)
st.write("The number of clusters set is", m)
