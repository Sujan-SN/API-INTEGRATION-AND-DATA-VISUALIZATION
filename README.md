# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: SUJAN S N

*INTERN ID*: CTIS6847

*DOMAIN*: Python Programming

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## DESCRIPTION OF THE TASK

This project demonstrates how to integrate a public API with Python and transform raw data into meaningful visual insights. The main objective of the task is to fetch real-time or forecast-based data from an external API and present it using clear and informative visualizations.

In this implementation, a weather-based API is used to retrieve environmental data such as temperature and humidity. The API acts as a bridge between the application and a remote server, allowing the program to access continuously updated datasets without storing them locally. By sending HTTP requests through Python, the program receives structured data in JSON format, which is then processed and analyzed.

The project begins with API integration using the requests library in Python. A GET request is sent to the API endpoint with required parameters such as location coordinates. Once the response is received, it is converted into JSON format for easy handling. The extracted dataset includes time-series information, which makes it suitable for trend analysis.

After fetching the data, the next step involves data preprocessing. The relevant attributes—such as timestamps, temperature values, and humidity levels—are filtered and stored in separate lists. To maintain clarity in visualization, only a subset of the data (for example, the first 10 time intervals) is selected. This ensures that the graphs remain readable and not overly cluttered.

For data visualization, the project uses Python libraries such as Matplotlib and Seaborn. These libraries provide powerful tools for creating aesthetically pleasing and informative charts. In this project, line plots are used to represent how temperature and humidity change over time. Each variable is plotted with distinct markers and labels, allowing easy comparison between the two datasets.

The visualization is designed as a simple dashboard, where multiple data trends are displayed in a single figure. The graph includes a title, axis labels, and a legend to improve interpretability. Rotating the x-axis labels ensures that timestamps are clearly visible, enhancing the overall user experience.

This project highlights the importance of combining data acquisition with visualization. While raw data alone may not provide immediate insights, graphical representation helps identify patterns, trends, and anomalies effectively. Such techniques are widely used in real-world applications, including weather forecasting, business analytics, and monitoring systems.

In conclusion, this task provides a foundational understanding of API integration and data visualization using Python. It demonstrates how external data sources can be accessed, processed, and transformed into meaningful visual outputs. The project also emphasizes practical skills such as working with APIs, handling JSON data, and creating visual dashboards, which are essential for modern data-driven applications.

## OUTPUT

<img width="1500" height="838" alt="Image" src="https://github.com/user-attachments/assets/1343879e-652e-4004-b796-683c126f2d0d" />
