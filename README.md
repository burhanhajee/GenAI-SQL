# AI Data Analyst - GenAI and SQL

## Introduction

In the ever-changing realm of data-driven decision-making, mastering the art of efficient and accurate database queries has become crucial. This project is a pioneering endeavour that merges advanced language technologies, specifically GPT 3.5 Turbo with Langchain Framework, with SQL databases. Our goal is to transform the traditional way of interacting with databases by facilitating more intuitive, efficient, and intelligent SQL query generation and processing.

Generative AI, a segment of artificial intelligence, is adept at creating new content, be it text, images, or code. In this project, the prowess of generative AI is harnessed to interpret inputs given in natural language and translate and execute them into complex SQL queries. This integration is not just about simplifying the query process; it's about making data analytics accessible to a wider audience, especially those not well-versed in SQL language. By simplifying the pathway to intricate database querying, I aim to democratize data analysis, making it more reachable and effective for everyone.

### Objectives:

- Integration of Language Models and SQL Databases: To demonstrate the effective integration of Langchain Framework using OpenAI's GPT 3.5 Turbo for improved query processing.
- Enhanced Query Formulation and Execution: To leverage language models for generating, interpreting, executing and optimizing SQL queries, enhancing the ease and efficiency of database querying.
- Semantic Analysis and Vectorization: To utilize semantic similarity and embeddings to understand and improve the relevance and accuracy of SQL queries.
- Practical Application in Real-World Scenarios: To apply this integration in practical scenarios, such as calculating profits, analyzing sales data, and optimizing inventory management.

## Literature Review: Generative AI in Data Analytics and Science Projects

In this literature review, we are looking into how Generative AI, or GenAI, is being used in data analytics and science projects. The focus is on two main sources that give us a good understanding of the current applications and potential of GenAI in this field.

#### [Deloitte AI Institute's Work](https://www2.deloitte.com/us/en/pages/consulting/articles/gen-ai-use-cases.html)

The Deloitte AI Institute has put together a set of use cases of GenAI across six different industries. This collection is very useful for getting ideas and understanding how GenAI can be used in different sectors. It's not just about having an advanced chatbot. GenAI can bring new ways of doing things, help in innovation, and even change how entire businesses work. Deloitte's work helps us see the broad possibilities of GenAI.

#### [AdEx Partners' Report](https://www.adexpartners.com/en/insights/implementing-data-analytics-science-projects-with-genai.html)

AdEx Partners discusses how GenAI can be used in data analytics and science projects, particularly in "co-piloting" roles. GenAI is valuable in saving time and effort in complex tasks like ETL specifications, ensuring data quality, and data modeling. This is a significant help for IT projects, where GenAI assists and adds to the expertise of humans throughout the project.

- Automated documentation
- Checking data quality
- Designing ETL processes
- Data modeling
- Testing
- Coding

However, it's also important to use GenAI in a balanced way, understanding its capabilities realistically and integrating it in a manner that focuses on client needs while considering risks and realistic expectations.
#### [LangChain for SQL Database Uses](https://python.langchain.com/docs/use_cases/sql/)

LangChain has special features that work with different kinds of SQL databases like MySQL, PostgreSQL, and others. It can do things like make queries from normal questions, make chatbots that use database information to answer questions, and build dashboards based on what users want to know. But, it's important to be careful with how the database connects to LangChain to avoid any risks.

#### [LangChain, LLMs, and SQL](https://blog.langchain.dev/llms-and-sql/)

There was a study by Rajkumar and others about how well OpenAI Codex works with SQL when you use different ways of asking it questions. They found that giving Codex SQL commands like CREATE TABLE with details about columns and types helps it perform better. It's also good to show examples of what the data looks like. LangChain uses these ideas from the study to make it work better.

#### [LangChain Agents, SQL, and OpenAI](https://blog.langchain.dev/how-to-safely-query-enterprise-data-with-langchain-agents-sql-openai-gretel/)

LangChain Agents can decide what tools to use based on what the user asks. For example, they can work with SQL databases. These agents use a method called MRKL to get information from the database and make SQL queries. The article also talks about making fake data that looks like real data but keeps it private using something called Gretel's models. They show that this fake data can be as good as real data for getting results.

## Data Description

The "Classic Models" dataset, commonly used in database and SQL training exercises, is a fictitious dataset representing a business scenario. It's designed to resemble a real-world database for a company that sells classic model cars. Here's an overview of this dataset:

### Data Structure

Tables: The database usually comprises several tables, each representing different aspects of the business. Common tables include:

- Customers
- Orders
- OrderDetails
- Products
- ProductLines
- Employees
- Offices

Relationships: These tables are often interconnected, with a complex relationship between each table which is excellent for Querying.

![Database Structure](images/db.png)

### Key Features

Important aspects of the dataset include:

- Products: Details about model cars, including product line, scale, and quantity in stock.
- Customers: Information on customers, including names, contact details, and credit limits.
- Orders and OrderDetails: Records of orders, including dates and item specifics.
- Employees: Data showing office, role, reporting structure, and contact information.
- Sales Territories: Information on sales offices and territories.

## Technology Overview

This section outlines the various technologies integrated into this project, each serving a unique purpose to enhance the functionality and user experience.

### `langchain` and `ChatGPT 3.5 Turbo`

These are central to integrating language models with other systems, including SQL databases. In this project, its responsible for the core functionality of formulating and processing SQL queries using language models.

- Seamless Integration: LangChain provides the necessary tools and functionalities to integrate language models like ChatGPT 3.5 Turbo with SQL databases effectively.
- Query Formulation and Processing: It facilitates the formulation of SQL queries from natural language inputs, making the most of ChatGPT 3.5 Turbo’s generative capabilities.
- Customization and Extension: LangChain’s modular design allows for customization and extension, enabling the project to incorporate specific features or experimental approaches as needed.

### `python-dotenv`

Manages environmental variables, such as database credentials or API keys, ensuring they are not hardcoded in your scripts for security reasons.

### `streamlit`

Used to create a web-based interface, allowing users to interact with the system in a more user-friendly and accessible manner.

### MySQL Connectors (`pymysql`)

These are MySQL database connectors, and at least one of them is used for establishing a connection to your MySQL database for query execution.

### `sentence-transformers`

Generates embeddings for sentences, texts, or words, crucial for semantic analysis and understanding the context of natural language inputs in your project.

### `HuggingFaceEmbeddings` from `sentence-transformers`

This model is used to create embeddings. It's a lightweight yet powerful model for generating sentence embeddings, capturing the semantic meanings of sentences.

### `Chroma` from `langchain.vectorstores`

Used for creating a vector store from the embeddings, facilitating enhanced data processing and analysis capabilities.

## Methodology

We start by setting up the LLM model, which forms the core of our system. To do this, we first need to securely access the OpenAI API key. Using the dotenv library, we can safely extract the API key from an environment file. This approach ensures that sensitive information, like API keys, is not hard-coded into our scripts, enhancing security and maintainability.

### Connecting to the Database

Once the LLM is ready, we connect to our SQL database using `langchain.utilities.SQLDatabase`. This step is crucial as it allows us to integrate the language model with our database, enabling the model to interact with and retrieve necessary data. Establishing this connection is the foundation for enabling the language model to generate SQL queries based on natural language input.

### Creating Few-Shot Examples

To guide the LLM in understanding the type of questions it will encounter, we create a set of "few-shot" examples. These examples consist of natural language questions, their corresponding SQL queries, and the expected results. This technique effectively "fine-tunes" the model by providing it with relevant, domain-specific examples. This step is critical as it helps in adapting the general capabilities of the LLM to our specific use case, thereby improving the accuracy of query generation.

Here are some sample examples:

```plaintext
few_shots = [
{'Question' : "Who reports to William Patterson?",
 'SQLQuery' : """SELECT CONCAT(reports.firstname, ' ', reports.lastname) AS Employee 
                 FROM Employees boss JOIN Employees reports ON boss.employeeNumber = reports.reportsTo 
                 WHERE boss.firstName = 'William' and boss.lastName = 'Patterson';""",
 'SQLResult': "Result of the SQL query",
 'Answer' : "'Andy Fixter', 'Peter Marsh', 'Tom King'"},
{'Question': "What are the top 3 products by quantity of on hand for products listed on 'On Hold' orders?" ,
 'SQLQuery' : """SELECT productName, FORMAT(quantityInStock,0) AS `Quantity in stock` 
                FROM OrderDetails JOIN Orders ON Orders.orderNumber = OrderDetails.orderNumber JOIN Products on OrderDetails.productCode = Products.productCode 
                WHERE status = 'On Hold' 
                ORDER BY quantityInStock desc limit 3;""",
 'SQLResult': "Result of the SQL query",
 'Answer': "'America West Airlines B757-200, 9,653', '2002 Chevy Corvette, 9,446', '1912 Ford Model T Delivery Wagon, 9,173'"} ,
{'Question': "Compute the commission for each sales representative, assuming the commission is 5% of the value of an order. Sort by employee last name and first name",
 'SQLQuery': """SELECT CONCAT(firstName, ' ',lastName) AS Name, FORMAT(.05 * SUM(quantityOrdered * priceEach),0) AS Commission
                FROM Employees JOIN Customers ON Employees.employeeNumber = Customers.salesRepEmployeeNumber
                JOIN Orders ON Customers.customerNumber = Orders.customerNumber
                JOIN OrderDetails ON Orders.orderNumber = OrderDetails.orderNumber
                GROUP BY employeeNumber
                ORDER BY lastName, firstName ASC;;",
                'SQLResult': "Result of the SQL query""",
                'Answer': "'Loui Bondur, 28,474', 'Larry Bott, 36,605', 'Pamela Castillo, 43,411', 'Julie Firrelli, 19,333','Andy Fixter, 28,129', 'Martin Gerard, 19,374'......"},
]'''

### Embeddings and Semantic Similarity Example Selection

Next, we move to the creation of embeddings for our few-shot examples. Embeddings are vector representations of text that capture the semantic meaning of the words. By converting our examples into embeddings, we enable the system to understand and compare the semantic similarity between different queries. This is beneficial as it helps the model in finding the most contextually relevant example for a given query, which in turn improves the quality of the SQL query generated.

After storing the embeddings in a Chroma database, we retrieve the most semantically similar example for a given query. This is achieved using a Semantic Similarity Example Selector. This selector uses the vectorized embeddings to find and return the examples that are closest in meaning to the input query. This step is essential as it allows the system to dynamically adapt to various queries by leveraging past examples, thus providing more accurate and relevant SQL translations for a wide range of natural language questions.

#### Semantic Similarity in Detail

The centerpiece of this integration is the Semantic Similarity Example Selector, a sophisticated component that significantly enhances query accuracy. It works by vectorizing past examples - pairing natural language questions with their corresponding SQL queries - and then selecting the most semantically similar examples for any new query. This methodology ensures that the generated SQL queries are contextually relevant and closely aligned with the user's intent. The system leverages historical data to learn and improve over time, reducing manual intervention and facilitating a more efficient query generation process.

For example, when I asked the SemanticSimilarityExampleSelector to find questions similar to the question, "Who reports to Mary Patterson?", the output contained the following 2 questions with respect to their Semantic Relevance:

- Who reports to William Patterson?
- Who are the employees in Boston?

As you can see, the model is capable of understanding that the new question could be solved by using the logic used in one of the sample questions. The second question is also extremely relevant as it's the only other question in the subset of questions which asks about the employee.

### Setting Up Prompt Templates and Model Building

The FewShotPromptTemplate in LangChain is used in this setup. It constructs prompts for the language model, incorporating semantically similar examples, the user's current query, and additional context like database schema information. This approach provides the model with a rich context, enabling it to understand and process complex queries more effectively. The template uses elements like example selectors and input variables to create comprehensive prompts, guiding the language model to produce accurate SQL queries. By automating the generation of context-aware SQL queries from natural language inputs, we can see the potential of AI in enhancing database querying and management, paving the way for innovative applications in various industries.

Continuing from the setup of the FewShotPromptTemplate, the next crucial step in the project involves the creation of a SQLDatabaseChain, which essentially stitches together the components we've established earlier into a coherent, functioning chain that can process queries. The SQLDatabaseChain is a powerful feature of LangChain that links the language model (LLM) with the SQL database, enabling the seamless translation of natural language queries into SQL queries.

### Model Performance and Observations

Here are some of the questions asked to the model:

**Question: What are the top 3 most profitable product lines**  
*SQLQuery: SELECT productLine AS `Product line`, FORMAT(SUM(quantityOrdered*(priceEach -buyPrice)),0) AS Profit FROM Products  
JOIN OrderDetails ON Products.productCode = OrderDetails.productCode  
GROUP BY productLine  
ORDER BY SUM(quantityOrdered*(priceEach -buyPrice)) DESC LIMIT 3;*  
Answer: 'Classic Cars, Vintage Cars, and Motorcycles with profits of $1,526,212, $737,268, and $469,255 respectively.  
This is the correct answer, with no problems that can be identified so far.
**Question: What is the percentage value of each product in inventory sorted by the highest percentage. Display only the top 5**  
*SQLQuery: SELECT productName, format(quantityInStock*buyPrice,0) AS Stock, format(quantityInStock*buyPrice/(totalValue)*100,2)  
AS Percent FROM Products, (SELECT SUM(quantityInStock*buyPrice) AS totalValue FROM Products) AS T ORDER BY quantityInStock*buyPrice/(totalValue)*100 DESC;*  
Answer: 2002 Suzuki XREO, 1.80%; 1995 Honda Civic, 1.76%; America West Airlines B757-200, 1.74%; 2002 Chevy Corvette, 1.70%; 1932 Model A Ford J-Coupe, 1.69%  
This is the correct answer, with no problems that can be identified so far.

**Question: Find the products sold in 2003 but not 2004.**  
*SQLQuery: SELECT productName FROM Products  
JOIN OrderDetails ON Products.productCode = OrderDetails.productCode  
JOIN Orders ON Orders.orderNumber = OrderDetails.orderNumber  
WHERE YEAR(orderDate) = 2003  
AND Products.productCode NOT IN  
(SELECT Products.productCode FROM Products  
JOIN OrderDetails ON Products.productCode = OrderDetails.productCode  
JOIN Orders ON Orders.orderNumber = OrderDetails.orderNumber  
WHERE YEAR(orderDate) = 2004);*  
Answer: 1952 Alpine Renault 1300, 1996 Moto Guzzi 1100i, 1993 Mazda RX-7, 1937 Lincoln Berline, 1936 Mercedes Benz 500k Roadster  
Although the model generates a query which provides us with the correct answer, the model "hallucinates" and provides an answer confidently - as the SQL Query Generates a null table but the model provided an incorrect list of products. The SQL Query is correct, however, the answer provided is completely made up. It is also important to note that the query can be improved. Here, "DISTINCT" can be used to avoid any duplicates, even if there are none, and the query can be more streamlined. A better query would be:  
*SELECT DISTINCT productName FROM Products  
JOIN OrderDetails ON Products.productCode = OrderDetails.productCode  
JOIN Orders ON OrderDetails.orderNumber = Orders.orderNumber  
WHERE YEAR(Orders.orderDate) = 2003  
AND Products.productCode NOT IN  
(SELECT productCode FROM OrderDetails  
JOIN Orders ON OrderDetails.orderNumber = Orders.orderNumber  
WHERE YEAR(Orders.orderDate) = 2004);*

**Key Differences in the queries:**
- **Use of DISTINCT:** The second query uses DISTINCT, ensuring unique product names. The first query might return duplicates if the same product was ordered multiple times in 2003. Although we know that the answer does not have any duplicates, it's a better practice to have correct queries.
- **Subquery Joins:** The first query's subquery includes a join with the Products table, which is redundant since the productCode is already available in OrderDetails. The second query's subquery is more efficient as it omits this unnecessary join.

**Question: Display the difference in the amount received for each month of 2004 compared to 2003?**  
*SQLQuery: SELECT FORMAT(SUM(amount),0) AS Difference FROM Payments WHERE YEAR(paymentDate) = 2004 GROUP BY MONTH(paymentDate)  
UNION  
SELECT FORMAT(SUM(amount),0) AS Difference FROM Payments WHERE YEAR(paymentDate) = 2003 GROUP BY MONTH(paymentDate);*  
The query generated combines the sum of payments for each month in 2004 and 2003 using a UNION. However, it does not directly compare the amounts between the two years, which was our question. Instead, it lists the sums for each month in 2004 followed by the sums for each month in 2003. It does not calculate the difference between the corresponding months of the two years.  
*Correct SQLQuery: WITH  
t2003 AS (SELECT YEAR(paymentDate) AS 'year', MONTH(paymentDate) AS 'month', sum(amount) AS amount FROM Payments  
WHERE YEAR(paymentDate) = 2003  
GROUP BY YEAR(paymentDate), MONTH(paymentDate)),  
t2004 AS (SELECT YEAR(paymentDate) AS 'year', MONTH(paymentDate) AS 'month', sum(amount) AS amount FROM Payments  
WHERE YEAR(paymentDate) = 2004  
GROUP BY YEAR(paymentDate), MONTH(paymentDate))  
SELECT t2003.month,format((t2004.amount - t2003.amount),2) AS variance  
FROM t2003 JOIN t2004  
ON t2003.month = t2004.month  
ORDER BY t2003.month;*  
The second query is more suitable to find the difference in payment amounts between corresponding months of 2003 and 2004. It directly compares the monthly sums of each year and calculates the variance.
## Limitations of using Langchain SQL Agent

- **Requires Extensive Training Data:** This short exploration of GenAI's application in Data Analytics has only underlined the necessity of High Quality Labelled Data, as opposed to relying solely on few-shot prompting. Extensive training data ensures that the model is exposed to a wide range of scenarios, nuances, and variations, allowing it to learn more comprehensive patterns and relationships. This depth of learning reduces the risk of errors and enhances the model's ability to understand contexts. Few-shot prompting, while useful for demonstrating a model's capabilities with limited examples, often lacks the breadth and depth needed for the model to perform reliably in complex, real-world situations.
- **AI Hallucination:** As we saw in one of the examples, AI can "create" incorrect or nonsensical answers due to limitations in training data. It happens because AI models, like neural networks, can make errors in interpreting input or extrapolating beyond their training. To control it, it's essential to use high-quality, diverse training data, implement robust error-checking mechanisms, and continuously update and refine the AI model to better understand context and real-world information.
- **Inability to Create and Show Visualizations and Tables:** Langchain SQL Agent is limited to generating SQL queries and cannot execute these queries to create and display visualizations or tables. Users need to manually execute the queries and use other tools for visualization and data presentation.
- **Understanding Complex Queries:** Langchain SQL Agent may have difficulty with very complex SQL queries, particularly those involving multiple nested subqueries, advanced functions, or complex joins.
- **Error Handling and Optimization:** The agent might not provide the most optimized queries for specific database environments, and users may need to modify queries for performance optimization and error handling.
- **Data Privacy and Security:** Since the agent generates queries based on user input, there's a reliance on the user to ensure data privacy and security standards are maintained. The agent itself doesn’t have mechanisms to enforce data security policies.

## Advantages and Use Cases of using Langchain SQL Agent

- **Automated Query Generation:** Langchain SQL Agent simplifies the process of writing SQL queries by automatically generating them based on natural language descriptions. This feature is particularly helpful for users who may not be well-versed in SQL syntax. It reduces the time and effort required to construct queries, especially for routine or repetitive tasks, thereby streamlining database interactions.
- **Ease of Use:** The agent's user-friendly interface allows users with varying levels of SQL expertise, including beginners, to interact with databases. By accepting inputs in natural language, it bridges the gap between non-technical users and complex database queries, making it easier for a broader audience to access and analyze data.
- **Rapid Prototyping:** The agent's ability to quickly generate SQL queries allows for rapid prototyping and experimentation. Users can efficiently test different data queries and hypotheses, which is particularly useful in exploratory data analysis. This capability enables faster iteration and refinement of queries, helping users to more quickly derive insights from their data.
- **Educational Tool:** I would highly recommend this for those learning SQL, as Langchain SQL Agent acts as a practical educational tool. By converting natural language descriptions into SQL queries, it provides real-time examples of how SQL syntax and structure work. As you progress and improve your skills, you can use a rusty model and correct the errors in the SQL Query Generated, helping to develop a deeper understanding of not just writing but also optimizing queries.
- **Productivity Boost:** The agent enhances productivity by handling the query generation aspect of database interaction. This allows users, especially those in data-driven roles, to allocate more time and focus to analyzing the results and deriving insights, rather than spending time on constructing and refining queries. For businesses and organizations, this can translate to quicker data-driven decision-making and more efficient use of resources.

## Future Updates to this Project

- **Dataset Curation and Labeling:** Make a carefully curated and labeled dataset to train the SQL Agent which ensures that the model learns a broad range of scenarios, data types, and complexities that are relevant to SQL query generation and data analysis. This should include varied examples of natural language inputs and corresponding correct SQL queries. Special attention will be given to edge cases and complex query structures.
- **Integrated Visualization Module:** Develop an integrated module that automatically executes SQL queries generated by the Langchain SQL Agent and visualizes the results. This module could include a variety of chart types (like bar charts, line graphs, pie charts) and table formats. It should be capable of handling different data types and structures. This update would significantly enhance the user experience by providing immediate, visually appealing representations of data, making it easier to interpret and analyze.
- **Execution and Optimization Engine:** Implement a backend system that not only executes the SQL queries but also optimizes them for performance. This engine could analyze the generated queries, suggest or automatically apply optimizations, and handle different database environments. This feature would ensure that queries run efficiently and effectively, especially important for large datasets or complex query structures.
- **Enhanced Error Detection and Feedback Mechanism:** Introduce an advanced error detection system that identifies potential issues in both the generated SQL queries and the visualizations. This system would provide meaningful feedback to users, suggesting corrections or improvements. Additionally, it could learn from these interactions, gradually improving the accuracy of the SQL query generation and the reliability of the visualizations.

