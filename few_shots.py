few_shots=few_shots = [
    {'Question' : "Who reports to William Patterson?",
     'SQLQuery' : "SELECT CONCAT(reports.firstname, ' ', reports.lastname) AS Employee FROM Employees boss JOIN Employees reports ON boss.employeeNumber = reports.reportsTo WHERE boss.firstName = 'William' and boss.lastName = 'Patterson';",
     'SQLResult': "Result of the SQL query",
     'Answer' : "'Andy Fixter', 'Peter Marsh', 'Tom King'"},
    {'Question': "Compute the commission for each sales representative, assuming the commission is 5% of the value of an order. Sort by employee last name and first name",
     'SQLQuery': "SELECT CONCAT(firstName, ' ',lastName) AS Name, FORMAT(.05 * SUM(quantityOrdered * priceEach),0) AS Commission FROM Employees JOIN Customers ON Employees.employeeNumber = Customers.salesRepEmployeeNumber JOIN Orders ON Customers.customerNumber = Orders.customerNumber JOIN OrderDetails ON Orders.orderNumber = OrderDetails.orderNumber GROUP BY employeeNumber ORDER BY lastName, firstName ASC;",
     'SQLResult': "Result of the SQL query",
     'Answer': "'Loui Bondur, 28,474', 'Larry Bott, 36,605', 'Pamela Castillo, 43,411', 'Julie Firrelli, 19,333','Andy Fixter, 28,129', 'Martin Gerard, 19,374'......"},
    {'Question': "What are the top 3 products by quantity of on hand for products listed on 'On Hold' orders?" ,
     'SQLQuery' : "SELECT productName, FORMAT(quantityInStock,0) AS `Quantity in stock` FROM OrderDetails JOIN Orders ON Orders.orderNumber = OrderDetails.orderNumber JOIN Products on OrderDetails.productCode = Products.productCode WHERE status = 'On Hold' order by quantityInStock desc limit 3;",
     'SQLResult': "Result of the SQL query",
     'Answer': "'America West Airlines B757-200, 9,653', '2002 Chevy Corvette, 9,446', '1912 Ford Model T Delivery Wagon, 9,173'"} ,
     {'Question' : "What is the value of orders shipped in August 2004?" ,
      'SQLQuery': "SELECT FORMAT(SUM(quantityOrdered*priceEach),0) as orderValue FROM Orders JOIN OrderDetails ON Orders.orderNumber = OrderDetails. orderNumber AND YEAR(orderDate) = 2004 AND MONTH(orderDate) = 8;",
      'SQLResult': "Result of the SQL query",
      'Answer' : '419,327'},
    {'Question': "What is the difference in the amount received for each month of 2004 compared to 2003?",
     'SQLQuery' : "WITH t2003 AS (SELECT YEAR(paymentDate) AS 'year', MONTH(paymentDate) AS 'month', sum(amount) AS amount FROM Payments WHERE YEAR(paymentDate) = 2003 GROUP BY YEAR(paymentDate), MONTH(paymentDate)), t2004 AS (SELECT YEAR(paymentDate) AS 'year', MONTH(paymentDate) AS 'month', sum(amount) AS amount FROM Payments WHERE YEAR(paymentDate) = 2004 GROUP BY YEAR(paymentDate), MONTH(paymentDate)) SELECT t2003.month,format((t2004.amount - t2003.amount),2) AS variance FROM t2003 JOIN t2004 ON t2003.month = t2004.month ORDER BY t2003.month;",
     'SQLResult': "Result of the SQL query",
     'Answer' : "'1, 207,884.51', '2, -37,732.35', '3, 204,898.73'"}
]