"""
Streamlit Data Analysis App

This is a complete Streamlit application demonstrating:
- Data loading and preprocessing
- Interactive visualizations
- Statistical analysis
- Machine learning basics
- Real-world data analysis workflow
"""

"""
# 📊 Data Analysis Dashboard

A comprehensive Streamlit application for data analysis and visualization.

## Features Demonstrated:
- Data upload and exploration
- Interactive charts and graphs
- Statistical analysis
- Data preprocessing
- Correlation analysis
- Basic machine learning
"""

# ============================================================================
# IMPORTS AND SETUP
# ============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="Data Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

st.sidebar.title("📊 Data Analysis Dashboard")
page = st.sidebar.radio(
    "Choose Analysis:",
    ["Data Upload", "Exploratory Analysis", "Visualization",
     "Statistical Analysis", "Correlation Analysis", "ML Predictions"]
)

# ============================================================================
# DATA UPLOAD PAGE
# ============================================================================

if page == "Data Upload":
    st.title("📁 Data Upload & Preview")

    st.markdown("""
    Upload your CSV or Excel file to begin analysis.
    If you don't have data, we'll use a sample dataset.
    """)

    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a CSV or Excel file",
        type=['csv', 'xlsx', 'xls']
    )

    # Sample data option
    use_sample = st.checkbox("Use sample dataset instead")

    @st.cache_data
    def load_sample_data():
        """Generate sample dataset for demonstration."""
        np.random.seed(42)
        n_samples = 1000

        data = {
            'age': np.random.normal(35, 10, n_samples).astype(int),
            'income': np.random.normal(50000, 15000, n_samples).astype(int),
            'education_years': np.random.normal(16, 3, n_samples).astype(int),
            'experience_years': np.random.normal(10, 5, n_samples).astype(int),
            'city': np.random.choice(['NYC', 'LA', 'Chicago', 'Houston', 'Boston'], n_samples),
            'department': np.random.choice(['Engineering', 'Sales', 'Marketing', 'HR', 'Finance'], n_samples),
            'satisfaction_score': np.random.uniform(1, 10, n_samples).round(1),
            'performance_rating': np.random.choice([1, 2, 3, 4, 5], n_samples, p=[0.1, 0.2, 0.4, 0.2, 0.1])
        }

        df = pd.DataFrame(data)

        # Add some realistic correlations
        df['income'] = df['income'] + df['experience_years'] * 2000 + df['education_years'] * 1000
        df['income'] = df['income'].clip(20000, 150000)

        return df

    # Load data
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.success(f"✅ Loaded {uploaded_file.name}")
        except Exception as e:
            st.error(f"❌ Error loading file: {e}")
            df = None
    elif use_sample:
        df = load_sample_data()
        st.info("ℹ️ Using sample dataset")
    else:
        df = None

    # Store data in session state
    if df is not None:
        st.session_state['data'] = df

        # Data preview
        st.subheader("📋 Data Preview")
        st.dataframe(df.head(10))

        # Basic info
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Rows", df.shape[0])
        with col2:
            st.metric("Columns", df.shape[1])
        with col3:
            st.metric("Missing Values", df.isnull().sum().sum())

        # Data types
        st.subheader("📝 Data Types")
        dtypes_df = pd.DataFrame({
            'Column': df.columns,
            'Type': df.dtypes,
            'Non-Null Count': df.count()
        })
        st.dataframe(dtypes_df)

# ============================================================================
# EXPLORATORY ANALYSIS PAGE
# ============================================================================

elif page == "Exploratory Analysis":
    st.title("🔍 Exploratory Data Analysis")

    if 'data' not in st.session_state:
        st.warning("⚠️ Please upload data first in the Data Upload section.")
    else:
        df = st.session_state['data']

        # Summary statistics
        st.subheader("📊 Summary Statistics")
        st.dataframe(df.describe())

        # Missing values analysis
        st.subheader("🔍 Missing Values Analysis")
        missing_data = df.isnull().sum()
        if missing_data.sum() > 0:
            missing_df = pd.DataFrame({
                'Column': missing_data.index,
                'Missing Count': missing_data.values,
                'Missing %': (missing_data.values / len(df) * 100).round(2)
            })
            st.dataframe(missing_df[missing_df['Missing Count'] > 0])

            # Handle missing values
            st.subheader("🛠️ Handle Missing Values")
            col_to_fill = st.selectbox("Select column to fill missing values:", df.columns[df.isnull().any()])

            if pd.api.types.is_numeric_dtype(df[col_to_fill]):
                fill_method = st.radio("Fill method:", ["Mean", "Median", "Mode", "Custom Value"])
                if fill_method == "Custom Value":
                    fill_value = st.number_input("Enter value:", value=0.0)
                elif fill_method == "Mean":
                    fill_value = df[col_to_fill].mean()
                elif fill_method == "Median":
                    fill_value = df[col_to_fill].median()
                else:  # Mode
                    fill_value = df[col_to_fill].mode().iloc[0]

                if st.button("Apply Fill"):
                    df[col_to_fill] = df[col_to_fill].fillna(fill_value)
                    st.session_state['data'] = df
                    st.success(f"✅ Filled missing values in {col_to_fill}")
            else:
                fill_value = st.text_input("Enter value to fill:")
                if st.button("Apply Fill"):
                    df[col_to_fill] = df[col_to_fill].fillna(fill_value)
                    st.session_state['data'] = df
                    st.success(f"✅ Filled missing values in {col_to_fill}")
        else:
            st.info("✅ No missing values found!")

        # Data distribution
        st.subheader("📈 Data Distribution")
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) > 0:
            selected_col = st.selectbox("Select numeric column for distribution:", numeric_cols)

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

            # Histogram
            ax1.hist(df[selected_col], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
            ax1.set_title(f'Histogram of {selected_col}')
            ax1.set_xlabel(selected_col)
            ax1.set_ylabel('Frequency')
            ax1.grid(True, alpha=0.3)

            # Box plot
            ax2.boxplot(df[selected_col], vert=False)
            ax2.set_title(f'Box Plot of {selected_col}')
            ax2.set_xlabel(selected_col)
            ax2.grid(True, alpha=0.3)

            plt.tight_layout()
            st.pyplot(fig)

# ============================================================================
# VISUALIZATION PAGE
# ============================================================================

elif page == "Visualization":
    st.title("📊 Data Visualization")

    if 'data' not in st.session_state:
        st.warning("⚠️ Please upload data first in the Data Upload section.")
    else:
        df = st.session_state['data']

        st.subheader("🎨 Interactive Charts")

        # Chart type selection
        chart_type = st.selectbox(
            "Select chart type:",
            ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram", "Box Plot", "Correlation Heatmap"]
        )

        if chart_type == "Scatter Plot":
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) >= 2:
                col1, col2 = st.columns(2)
                with col1:
                    x_col = st.selectbox("X-axis:", numeric_cols, key="scatter_x")
                with col2:
                    y_col = st.selectbox("Y-axis:", numeric_cols, key="scatter_y")

                color_col = st.selectbox("Color by (optional):", ["None"] + df.columns.tolist())

                if color_col == "None":
                    fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
                else:
                    fig = px.scatter(df, x=x_col, y=y_col, color=color_col,
                                   title=f"{y_col} vs {x_col} (colored by {color_col})")

                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Need at least 2 numeric columns for scatter plot")

        elif chart_type == "Bar Chart":
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            categorical_cols = df.select_dtypes(include=['object', 'category']).columns

            if len(categorical_cols) > 0 and len(numeric_cols) > 0:
                cat_col = st.selectbox("Category column:", categorical_cols)
                num_col = st.selectbox("Value column:", numeric_cols)

                # Group and aggregate
                grouped_data = df.groupby(cat_col)[num_col].mean().reset_index()

                fig = px.bar(grouped_data, x=cat_col, y=num_col,
                           title=f"Average {num_col} by {cat_col}")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Need both categorical and numeric columns")

        elif chart_type == "Histogram":
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                col = st.selectbox("Select column:", numeric_cols)
                bins = st.slider("Number of bins:", 5, 50, 20)

                fig = px.histogram(df, x=col, nbins=bins,
                                 title=f"Distribution of {col}")
                st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Box Plot":
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            categorical_cols = df.select_dtypes(include=['object', 'category']).columns

            if len(numeric_cols) > 0:
                num_col = st.selectbox("Numeric column:", numeric_cols)

                if len(categorical_cols) > 0:
                    cat_col = st.selectbox("Group by (optional):", ["None"] + categorical_cols.tolist())
                    if cat_col != "None":
                        fig = px.box(df, x=cat_col, y=num_col,
                                   title=f"{num_col} distribution by {cat_col}")
                    else:
                        fig = px.box(df, y=num_col, title=f"{num_col} distribution")
                else:
                    fig = px.box(df, y=num_col, title=f"{num_col} distribution")

                st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Correlation Heatmap":
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) >= 2:
                corr_matrix = df[numeric_cols].corr()

                fig = go.Figure(data=go.Heatmap(
                    z=corr_matrix.values,
                    x=corr_matrix.columns,
                    y=corr_matrix.columns,
                    colorscale='RdBu',
                    zmin=-1, zmax=1
                ))

                fig.update_layout(
                    title="Correlation Heatmap",
                    xaxis_title="Features",
                    yaxis_title="Features"
                )

                st.plotly_chart(fig, use_container_width=True)

                # Display correlation values
                st.subheader("Correlation Values")
                st.dataframe(corr_matrix.round(3))
            else:
                st.warning("Need at least 2 numeric columns for correlation analysis")

# ============================================================================
# STATISTICAL ANALYSIS PAGE
# ============================================================================

elif page == "Statistical Analysis":
    st.title("📈 Statistical Analysis")

    if 'data' not in st.session_state:
        st.warning("⚠️ Please upload data first in the Data Upload section.")
    else:
        df = st.session_state['data']

        st.subheader("📊 Basic Statistics")

        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) > 0:
            selected_cols = st.multiselect(
                "Select columns for analysis:",
                numeric_cols,
                default=numeric_cols[:3] if len(numeric_cols) >= 3 else numeric_cols
            )

            if selected_cols:
                stats_df = df[selected_cols].describe()

                # Add additional statistics
                additional_stats = pd.DataFrame({
                    'skewness': df[selected_cols].skew(),
                    'kurtosis': df[selected_cols].kurtosis(),
                    'variance': df[selected_cols].var(),
                    'range': df[selected_cols].max() - df[selected_cols].min()
                }).T

                full_stats = pd.concat([stats_df, additional_stats])
                st.dataframe(full_stats.round(3))

                # Outlier detection
                st.subheader("🔍 Outlier Detection")

                for col in selected_cols:
                    Q1 = df[col].quantile(0.25)
                    Q3 = df[col].quantile(0.75)
                    IQR = Q3 - Q1

                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR

                    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]

                    st.write(f"**{col}:** {len(outliers)} outliers detected")
                    if len(outliers) > 0:
                        st.write(f"Outlier values: {outliers.values}")

# ============================================================================
# CORRELATION ANALYSIS PAGE
# ============================================================================

elif page == "Correlation Analysis":
    st.title("🔗 Correlation Analysis")

    if 'data' not in st.session_state:
        st.warning("⚠️ Please upload data first in the Data Upload section.")
    else:
        df = st.session_state['data']

        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) >= 2:
            # Correlation matrix
            corr_matrix = df[numeric_cols].corr()

            # Heatmap
            fig = go.Figure(data=go.Heatmap(
                z=corr_matrix.values,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                colorscale='RdBu',
                zmin=-1, zmax=1,
                text=corr_matrix.round(2).values,
                texttemplate='%{text}',
                textfont={"size": 10},
                hoverongaps=False
            ))

            fig.update_layout(
                title="Correlation Matrix",
                xaxis_title="Features",
                yaxis_title="Features",
                width=800,
                height=800
            )

            st.plotly_chart(fig)

            # Strong correlations
            st.subheader("🎯 Strong Correlations (|correlation| > 0.5)")

            strong_corr = []
            for i in range(len(corr_matrix.columns)):
                for j in range(i+1, len(corr_matrix.columns)):
                    corr_val = corr_matrix.iloc[i, j]
                    if abs(corr_val) > 0.5:
                        strong_corr.append({
                            'Variable 1': corr_matrix.columns[i],
                            'Variable 2': corr_matrix.columns[j],
                            'Correlation': corr_val
                        })

            if strong_corr:
                strong_corr_df = pd.DataFrame(strong_corr).sort_values('Correlation', key=abs, ascending=False)
                st.dataframe(strong_corr_df.round(3))
            else:
                st.info("No strong correlations found (|correlation| > 0.5)")

            # Scatter plots for correlated pairs
            st.subheader("📊 Scatter Plots for Correlated Pairs")

            if strong_corr:
                pair_options = [f"{pair['Variable 1']} vs {pair['Variable 2']}" for pair in strong_corr]
                selected_pair = st.selectbox("Select pair to visualize:", pair_options)

                pair_idx = pair_options.index(selected_pair)
                var1 = strong_corr[pair_idx]['Variable 1']
                var2 = strong_corr[pair_idx]['Variable 2']

                fig = px.scatter(df, x=var1, y=var2,
                               title=f"{var1} vs {var2} (r = {strong_corr[pair_idx]['Correlation']:.3f})",
                               trendline="ols")
                st.plotly_chart(fig, use_container_width=True)

        else:
            st.warning("Need at least 2 numeric columns for correlation analysis")

# ============================================================================
# ML PREDICTIONS PAGE
# ============================================================================

elif page == "ML Predictions":
    st.title("🤖 Machine Learning Predictions")

    if 'data' not in st.session_state:
        st.warning("⚠️ Please upload data first in the Data Upload section.")
    else:
        df = st.session_state['data']

        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) >= 2:
            st.subheader("🔮 Linear Regression Model")

            # Select target and features
            target_col = st.selectbox("Select target variable (to predict):", numeric_cols)

            feature_cols = st.multiselect(
                "Select feature variables:",
                [col for col in numeric_cols if col != target_col],
                default=[col for col in numeric_cols if col != target_col][:3]
            )

            if feature_cols:
                # Prepare data
                X = df[feature_cols]
                y = df[target_col]

                # Handle missing values
                X = X.fillna(X.mean())
                y = y.fillna(y.mean())

                # Split data
                test_size = st.slider("Test set size (%):", 10, 50, 20) / 100
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=test_size, random_state=42
                )

                # Train model
                model = LinearRegression()
                model.fit(X_train, y_train)

                # Make predictions
                y_pred = model.predict(X_test)

                # Model evaluation
                mse = mean_squared_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Mean Squared Error", f"{mse:.2f}")
                with col2:
                    st.metric("R² Score", f"{r2:.3f}")
                with col3:
                    st.metric("Test Set Size", f"{len(X_test)} samples")

                # Feature importance
                st.subheader("📊 Feature Importance")
                feature_importance = pd.DataFrame({
                    'Feature': feature_cols,
                    'Coefficient': model.coef_
                }).sort_values('Coefficient', key=abs, ascending=False)

                fig = px.bar(feature_importance, x='Feature', y='Coefficient',
                           title="Feature Coefficients")
                st.plotly_chart(fig, use_container_width=True)

                # Predictions vs Actual
                st.subheader("🎯 Predictions vs Actual")
                pred_df = pd.DataFrame({
                    'Actual': y_test,
                    'Predicted': y_pred
                })

                fig = px.scatter(pred_df, x='Actual', y='Predicted',
                               title="Predicted vs Actual Values")
                fig.add_trace(go.Scatter(x=[pred_df['Actual'].min(), pred_df['Actual'].max()],
                                       y=[pred_df['Actual'].min(), pred_df['Actual'].max()],
                                       mode='lines', name='Perfect Prediction',
                                       line=dict(color='red', dash='dash')))
                st.plotly_chart(fig, use_container_width=True)

                # Make new predictions
                st.subheader("🔮 Make New Predictions")

                col1, col2 = st.columns(2)
                input_values = {}

                for i, feature in enumerate(feature_cols):
                    if i % 2 == 0:
                        with col1:
                            input_values[feature] = st.number_input(
                                f"{feature}:",
                                value=float(df[feature].mean()),
                                key=f"input_{feature}"
                            )
                    else:
                        with col2:
                            input_values[feature] = st.number_input(
                                f"{feature}:",
                                value=float(df[feature].mean()),
                                key=f"input_{feature}"
                            )

                if st.button("Predict"):
                    input_df = pd.DataFrame([input_values])
                    prediction = model.predict(input_df)[0]
                    st.success(f"Predicted {target_col}: {prediction:.2f}")

        else:
            st.warning("Need at least 2 numeric columns for machine learning")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("*Built with Streamlit, Pandas, NumPy, Scikit-learn, and Plotly*")
st.markdown("*Upload your data or use the sample dataset to explore all features!*")
