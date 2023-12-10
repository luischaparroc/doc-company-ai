GENERAL_COMPANY_CONTEXT = """
PayApp is a fintech startup company.
The mission of the company PayApp is to provide to all the people a way to do payments easily.
The company develops an in-house mobile application available in IOS and Android operating systems.

The company is a LLC registered in Delaware, United States. It was founded in 2021 by three people:
- Robert Horowitz: Chief Executive Officer
- Vicente Tellez: Chief Operations Officer
- Walter Rubin: Chief Technology Officer

The company has 7 departments:

- Technology: This department is responsible for developing the systems of the mobile application and the data architecture.
              The leader of the department is Sam Brunswick (Head of Technology).
              There are 11 employees in this department.

- Customer Service: This department is responsible for attending customer issues or answering customer questions.
                    The leader of the department is Jennifer Bold (VicePresident of Customer Success).
                    There are 8 employees in this department.

- People: This department is responsible for Human Resources purposes.
          The leader of the department is Janeth Reyes (Head of People).
          There are 5 employees in this department

- Finance: This department is responsible for accounting and financial purposes.
           The leader of the department is Luis Rodriguez (VicePresident of Finance).
           There are 4 employees in this department.

- Legal: This department is responsible for creating legal terms.
         The leader of the department is Mark Smith (Head of Legal).
         There are 2 employees in this department.

- Marketing: This department is responsible for creating new campaigns to get new customers.
             The leader of the department is Marie Watson (Head of Marketing).
             There are 8 employees in this department.

- Product: This department is responsible for creating or updating the products that the company provides.
           The leader of the department is Lex Friedman (Head of Product).
           There are 9 employees in this department.

The company has presence in United States, Mexico and Colombia markets.
Right now, there are 50 people in the company and the goal is to hire other 50 people.
This people work from United States (the HQ offices are located in New York), Mexico and Colombia (remote).

"""

COMPANY_PROMPT = f"""
Imagine you are a technical writer of startup fintech company called PayApp.

Based in the provided information, your task is to generate documentation with the following topics:

- Company Mission and History
- Company Business Model
- Chief Staff, with their names and their email addresses (assume the address is first_name.last_name@payapp.com)
- The number of employees of the company
- The number of employees of the company

The documentation is intended to provide more context to the employees, so they can understand better the business model and the mission of the company.

Use at most 300 words.

Company information: ```{GENERAL_COMPANY_CONTEXT}```
"""

TECHNOLOGY_PROMPT = f"""
Imagine you are a technical writer of startup fintech company called PayApp.

Based in the provided information, your task is to create a documentation explaining the following topics related to the Technology Department:

- Mission of the department
- Developed applications, with their architecture and the technology stack.
- Leader of the department, with his/her name and the email addresses (assume the address is first_name.last_name@payapp.com)
- Number of employees

The description is intended to help the employees to understand the work done by the technology department. In this way, they can have more context.

Use at most 300 words.

Company information: ```{GENERAL_COMPANY_CONTEXT}```
"""

CUSTOMER_SUCCESS_PROMPT = f"""
Imagine you are a technical writer of startup fintech company called PayApp.

Based in the provided information, your task is to create a documentation explaining the following topics related to the customer success department:

- Mission of the department
- Common issues or answers that the people of the department provide.
- Leader of the department, with his/her name and the email addresses (assume the address is first_name.last_name@payapp.com)
- Number of employees

The description is intended to help the employees to understand the work done by the customer success department. In this way, they can have more context.

Use at most 300 words.

Company information: ```{GENERAL_COMPANY_CONTEXT}```
"""

PEOPLE_PROMPT = f"""
Imagine you are a technical writer of startup fintech company called PayApp.

Based in the provided information, your task is to create a documentation explaining the following topics related to the people department:

- Mission of the department
- Defined policies for vacations, personal time off and benefits.
- Leader of the department, with his/her name and the email addresses (assume the address is first_name.last_name@payapp.com)
- Number of employees

The description is intended to help the employees to understand the work done by the people department. In this way, they can have more context.

Use at most 600 words.

Company information: ```{GENERAL_COMPANY_CONTEXT}```
"""

FINANCE_PROMPT = f"""
Imagine you are a technical writer of startup fintech company called PayApp.

Based in the provided information, your task is to create a documentation explaining the following topics related to the finance department:

- Mission of the department
- Defined policies for payments and accounting.
- Leader of the department, with his/her name and the email addresses (assume the address is first_name.last_name@payapp.com)
- Number of employees

The description is intended to help the employees to understand the work done by the finance department. In this way, they can have more context.

Use at most 300 words.

Company information: ```{GENERAL_COMPANY_CONTEXT}```
"""

LEGAL_PROMPT = f"""
Imagine you are a technical writer of startup fintech company called PayApp.

Based in the provided information, your task is to create a documentation explaining the following topics related to the legal department:

- Mission of the department
- Defined non disclosure agreements by the department.
- Leader of the department, with his/her name and the email addresses (assume the address is first_name.last_name@payapp.com)
- Number of employees

The description is intended to help the employees to understand the work done by the legal department. In this way, they can have more context.

Use at most 300 words.

Company information: ```{GENERAL_COMPANY_CONTEXT}```
"""

MARKETING_PROMPT = f"""
Imagine you are a technical writer of startup fintech company called PayApp.

Based in the provided information, your task is to create a documentation explaining the following topics related to the marketing department:

- Mission of the department
- Developed marketing campaigns
- Leader of the department, with his/her name and the email addresses (assume the address is first_name.last_name@payapp.com)
- Number of employees

The description is intended to help the employees to understand the work done by the marketing department. In this way, they can have more context.

Use at most 400 words.

Company information: ```{GENERAL_COMPANY_CONTEXT}```
"""


PRODUCT_PROMPT = f"""
Imagine you are a technical writer of startup fintech company called PayApp.

Based in the provided information, your task is to create a documentation explaining the following topics related to the product department:

- Mission of the department
- Developed product applications
- Leader of the department, with his/her name and the email addresses (assume the address is first_name.last_name@payapp.com)
- Number of employees

The description is intended to help the employees to understand the work done by the product department. In this way, they can have more context.

Use at most 400 words.

Company information: ```{GENERAL_COMPANY_CONTEXT}```
"""
