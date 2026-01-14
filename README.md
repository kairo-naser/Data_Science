# Data Science Portfolio: Core Python Modules

This repository contains a collection of Python scripts and documentation covering the essential libraries and techniques for Data Science, based on the course curriculum for Web Scraping, NumPy, Pandas, and Data Visualization.

---

## 📚 Modules Overview

### 1. Web Scraping (`BeautifulSoup` & `Requests`)
Extracting data from the web using automated scripts.
* **Tools:** `requests`, `BeautifulSoup`, `html5lib`.
* **Key Tasks:** Sending HTTP requests, parsing nested HTML structures, and cleaning table data by removing HTML tags.

### 2. Numerical Computing (`NumPy`)
The foundation for high-performance scientific computing.
* **Concepts:** Multidimensional arrays (`ndarray`), fixed data types, and vectorization.
* **Key Functions:** Array creation (`arange`, `ones`, `empty`), statistical analysis (`std`, `var`), and matrix transposing.



### 3. Data Analysis (`Pandas`)
Structured data manipulation using labeled axes.
* **Data Structures:** Series (1D) and DataFrames (2D).
* **Key Tasks:** Loading CSVs, descriptive statistics (`describe`), and managing missing data using `isnull()` and `fillna()`.

### 4. Data Wrangling (Cleaning & Enrichment)
Transforming raw data into a format suitable for analysis.
* **Cleaning:** Renaming columns, casting data types (Categorical/Datetime), and sorting.
* **Enrichment:** Data splitting, deduplication, and datetime-based slicing.



### 5. Data Visualization (`Matplotlib`)
Communicating insights through graphical representations.
* **Hierarchy:** Figure vs. Axes objects.
* **Plots:** Line charts, Scatter plots, and Bar graphs.
* **Layouts:** Creating multi-plot figures using the `subplot` system.



---

## 🛠️ Installation & Setup

To run these scripts locally, install the required dependencies using pip:

```bash
pip install numpy pandas matplotlib beautifulsoup4 requests html5lib lxml