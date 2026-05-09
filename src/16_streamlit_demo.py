"""
Python Streamlit Concepts

This module demonstrates Streamlit fundamentals:
- Basic app structure
- Widgets and user input
- Data display
- Layout and containers
- Caching and performance
- State management
"""

# Note: This is a demonstration file showing Streamlit concepts
# To run this, install streamlit: pip install streamlit
# Then run: streamlit run streamlit_demo.py

"""
# Streamlit Demo App

This file contains examples of Streamlit features.
To run this app, save it as 'streamlit_demo.py' and run:
streamlit run streamlit_demo.py

Below are the key concepts demonstrated:
"""

# ============================================================================
# BASIC STREAMLIT APP STRUCTURE
# ============================================================================

"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page configuration (must be first Streamlit command)
st.set_page_config(
    page_title="Python Concepts Demo",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and header
st.title("🐍 Python Programming Concepts Demo")
st.header("Interactive Learning Platform")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a topic:", [
    "Home", "Data Types", "NumPy", "Pandas", "Visualization"
])

# Main content based on selection
if page == "Home":
    st.write("Welcome to the Python Concepts interactive demo!")
    st.markdown("""
    This app demonstrates various Python programming concepts including:
    - Data types and structures
    - NumPy array operations
    - Pandas data manipulation
    - Data visualization
    """)

elif page == "Data Types":
    st.header("Python Data Types")
    st.write("Explore different Python data types:")

    # Interactive examples
    data_type = st.selectbox(
        "Choose a data type:",
        ["Integer", "Float", "String", "List", "Dictionary", "Set"]
    )

    if data_type == "Integer":
        num = st.number_input("Enter an integer:", value=42)
        st.write(f"You entered: {num}")
        st.write(f"Type: {type(num)}")
        st.write(f"Is even: {num % 2 == 0}")

    elif data_type == "String":
        text = st.text_input("Enter some text:", "Hello, World!")
        st.write(f"You entered: '{text}'")
        st.write(f"Length: {len(text)}")
        st.write(f"Uppercase: {text.upper()}")
        st.write(f"Reversed: {text[::-1]}")

    elif data_type == "List":
        st.write("List operations:")
        items = st.text_area("Enter comma-separated items:", "apple,banana,cherry")
        item_list = [item.strip() for item in items.split(",")]
        st.write(f"List: {item_list}")
        st.write(f"Length: {len(item_list)}")

        if st.button("Sort list"):
            sorted_list = sorted(item_list)
            st.write(f"Sorted: {sorted_list}")

elif page == "NumPy":
    st.header("NumPy Array Operations")

    st.write("Create and manipulate NumPy arrays:")

    # Array creation
    size = st.slider("Array size:", 1, 20, 5)
    arr = np.random.randint(1, 100, size)
    st.write(f"Random array: {arr}")

    # Operations
    operation = st.selectbox(
        "Choose operation:",
        ["Sum", "Mean", "Max", "Min", "Sort"]
    )

    if operation == "Sum":
        result = np.sum(arr)
        st.write(f"Sum: {result}")
    elif operation == "Mean":
        result = np.mean(arr)
        st.write(f"Mean: {result:.2f}")
    elif operation == "Max":
        result = np.max(arr)
        st.write(f"Maximum: {result}")
    elif operation == "Min":
        result = np.min(arr)
        st.write(f"Minimum: {result}")
    elif operation == "Sort":
        result = np.sort(arr)
        st.write(f"Sorted: {result}")

    # Matrix operations
    st.subheader("Matrix Operations")
    matrix_size = st.slider("Matrix size:", 2, 5, 3)

    A = np.random.randint(1, 10, (matrix_size, matrix_size))
    B = np.random.randint(1, 10, (matrix_size, matrix_size))

    col1, col2 = st.columns(2)
    with col1:
        st.write("Matrix A:")
        st.write(A)
    with col2:
        st.write("Matrix B:")
        st.write(B)

    if st.button("Matrix Multiplication"):
        result = A @ B
        st.write("A × B:")
        st.write(result)

elif page == "Pandas":
    st.header("Pandas DataFrame Operations")

    # Create sample data
    @st.cache_data
    def create_sample_data():
        return pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
            'Age': [25, 30, 35, 28, 32],
            'City': ['NYC', 'LA', 'Chicago', 'Houston', 'Boston'],
            'Salary': [50000, 60000, 70000, 55000, 65000],
            'Department': ['Engineering', 'Sales', 'Marketing', 'Engineering', 'HR']
        })

    df = create_sample_data()

    st.write("Sample Employee Data:")
    st.dataframe(df)

    # Filtering
    st.subheader("Data Filtering")

    min_age = st.slider("Minimum age:", 20, 40, 25)
    filtered_df = df[df['Age'] >= min_age]
    st.write(f"Employees aged {min_age}+:")
    st.dataframe(filtered_df)

    # Department selection
    departments = st.multiselect(
        "Select departments:",
        df['Department'].unique(),
        default=df['Department'].unique()
    )
    dept_filtered = df[df['Department'].isin(departments)]
    st.write("Filtered by department:")
    st.dataframe(dept_filtered)

    # Statistics
    st.subheader("Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Age", f"{df['Age'].mean():.1f}")
    with col2:
        st.metric("Average Salary", f"${df['Salary'].mean():.0f}")
    with col3:
        st.metric("Total Employees", len(df))

    # Group by operations
    st.subheader("Department Statistics")
    dept_stats = df.groupby('Department').agg({
        'Salary': ['mean', 'count'],
        'Age': 'mean'
    }).round(2)
    st.dataframe(dept_stats)

elif page == "Visualization":
    st.header("Data Visualization")

    # Generate sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.linspace(0, 10, 100),
        'y1': np.sin(np.linspace(0, 10, 100)),
        'y2': np.cos(np.linspace(0, 10, 100)),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })

    # Line plot
    st.subheader("Line Plot")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['x'], data['y1'], label='sin(x)', color='blue')
    ax.plot(data['x'], data['y2'], label='cos(x)', color='red')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Scatter plot
    st.subheader("Scatter Plot")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    scatter = ax2.scatter(data['x'], data['y1'],
                         c=data['x'], cmap='viridis',
                         alpha=0.6)
    ax2.set_xlabel('X')
    ax2.set_ylabel('sin(X)')
    plt.colorbar(scatter, ax=ax2)
    st.pyplot(fig2)

    # Bar chart
    st.subheader("Bar Chart")
    category_counts = data['category'].value_counts()
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    ax3.bar(category_counts.index, category_counts.values,
            color=['skyblue', 'lightgreen', 'salmon'])
    ax3.set_xlabel('Category')
    ax3.set_ylabel('Count')
    ax3.set_title('Category Distribution')
    st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit - Interactive Python Web Apps*")

# ============================================================================
# STREAMLIT WIDGETS REFERENCE
# ============================================================================

"""
# Streamlit Widgets Reference

## Input Widgets
- `st.text_input()` - Single line text input
- `st.text_area()` - Multi-line text input
- `st.number_input()` - Numeric input
- `st.slider()` - Slider for numeric values
- `st.selectbox()` - Dropdown selection
- `st.multiselect()` - Multiple selection
- `st.checkbox()` - Boolean checkbox
- `st.radio()` - Radio button selection
- `st.button()` - Clickable button
- `st.file_uploader()` - File upload

## Display Widgets
- `st.write()` - General display (supports multiple types)
- `st.markdown()` - Markdown text
- `st.latex()` - LaTeX mathematical expressions
- `st.code()` - Code display with syntax highlighting
- `st.dataframe()` - Interactive DataFrame display
- `st.table()` - Static table display
- `st.json()` - JSON data display
- `st.metric()` - Metric display with delta
- `st.pyplot()` - Matplotlib plot display

## Layout Widgets
- `st.columns()` - Create column layout
- `st.container()` - Group widgets in a container
- `st.sidebar` - Sidebar layout
- `st.tabs()` - Tabbed interface
- `st.expander()` - Expandable section

## Media Widgets
- `st.image()` - Display images
- `st.audio()` - Play audio files
- `st.video()` - Play video files

## State Management
- `st.session_state` - Persistent state across reruns
- `@st.cache_data` - Cache expensive computations
- `@st.cache_resource` - Cache resources like database connections

## Advanced Features
- `st.form()` - Batch input processing
- `st.progress()` - Progress bar
- `st.spinner()` - Loading spinner
- `st.error()`, `st.warning()`, `st.info()`, `st.success()` - Status messages
"""

# ============================================================================
# SUMMARY
# ============================================================================

"""
# Key Takeaways for Streamlit

1. **Simple API**: Turn Python scripts into web apps with minimal code
2. **Reactive**: App updates automatically when user interacts with widgets
3. **Data Display**: Rich support for DataFrames, charts, and visualizations
4. **Layout Control**: Columns, sidebars, tabs, and containers for organization
5. **Caching**: `@st.cache_data` and `@st.cache_resource` for performance
6. **State Management**: `st.session_state` for maintaining app state
7. **File Handling**: Built-in support for file uploads and downloads
8. **Deployment**: Easy deployment to Streamlit Cloud, Heroku, etc.
9. **Integration**: Works seamlessly with pandas, numpy, matplotlib, etc.
10. **Real-time**: Perfect for data exploration and interactive dashboards
"""
