from datetime import datetime
import json
import re

# Create your views here.
def Job_Salary(job):

    #Formatting
    min_salary = None
    max_salary = None
    price_range = None
    timeframe = 0
    paymentScheme = ['Salary','Per Hour','Per Day','Per Annuam']

    #Identification Phase 
    if "minimumSalary" in job:
        if job["minimumSalary"] is not None:
            min_salary = job['minimumSalary']
            max_salary = job['maximumSalary']

    elif 'salary' in job:
        if job['salary'] is not None:
            salary = re.sub(r'[^0-9]', ' ', job['salary'])
            salary = salary.split()
            if(len(salary) == 2):
                min_salary = salary[0]
                max_salary = salary[1]
            else:
                min_salary = salary[0]
                max_salary = salary[0]

    #Conversion part
    if min_salary is not None and max_salary is not None:
        timeframe = 0
        min_salary = float(min_salary)
        max_salary = float(max_salary)

        #Identify price range
        if  0 <= min_salary <= 70:
            string_min_salary = format(min_salary, '.2f')
            string_max_salary = format(max_salary, '.2f')
            timeframe = 1

        elif 70 <= min_salary <= 999:
            string_min_salary = int(min_salary)
            string_max_salary = int(max_salary)
            timeframe = 2 

        else:
            string_min_salary = int(min_salary)
            string_max_salary = int(max_salary)
            string_min_salary = "{:,}".format(string_min_salary)
            string_max_salary = "{:,}".format(string_max_salary)
            timeframe = 3

        #String representation price range
        if max_salary != min_salary:
            price_range = '£'+str(string_min_salary)+ ' - £'+str(string_max_salary)
        else: 
            price_range = '£'+str(string_min_salary)

    else:
        price_range = 'Competitive salary'

    salaryDict = {}
    salaryDict['price_range'] = price_range
    salaryDict['paymentScheme'] = paymentScheme[timeframe]
    salaryDict['min_salary'] = min_salary
    salaryDict['max_salary'] = max_salary

    return salaryDict

def Job_Posted(posted_date):
    #formatting stage 
    posted_date = posted_date[:10]

    #identification
    if '-' in posted_date:
        posted_date = posted_date.replace("-", "/")
        posted_date = datetime.strptime(posted_date, "%Y/%m/%d")
    else:
        posted_date = datetime.strptime(posted_date, "%d/%m/%Y")

    month = posted_date.strftime("%B")
    day = posted_date.day
    return f'{month} {day}'

def Job_Logo(*args):

    try:
        job_company_logo = args[0]['logo']
    except:
        job_company_logo = 'https://static.vecteezy.com/system/resources/previews/002/292/395/original/placeholder-on-map-line-outline-icon-for-website-and-mobile-app-on-grey-background-free-vector.jpg'
    
    return job_company_logo

# def Job_Salary(request,job,config):
#     annual_salary = ""
#     min_salary = None

#     #Identification Phase 
#     match config:
#         case 1:
#             min_salary = job['minimumSalary']
#             max_salary = job['maximumSalary']

#         case 2:
            
#             #Timeframe Payroll
#             if '/hour' in job:
#                 hourly = True
#             if '/annum' in job:
#                 hourly = False

#             #Great Filter
#             salary_list = []
#             for item in job.split():
#                 numeric_filter = filter(str.isdigit, item)
#                 item = "".join(numeric_filter)
#                 if (item != ""):
#                     if hourly == True:
#                         item = float(item)/100
#                     salary_list.append(item)
#             job = salary_list

#             match len(job):
#                 case 1:
#                     min_salary = job[0]
#                     max_salary = job[0]
#                 case 2:
#                     min_salary = job[1]
#                     max_salary = job[0]


#         case _:
#             annual_salary = 'Competitive salary'


#     #Formatting Phase
#     try:
#         #remove .00 from salary
#         #Min and max dymanics
#         min_salary = int(min_salary)   
#         max_salary = int(max_salary)   
#         min_salary = "{:,}".format(min_salary)
#         max_salary = "{:,}".format(max_salary)

#         #Per Hour
#         if len(str(min_salary)) <= 2:
#             annual_salary = '£'+str(min_salary)+ ' - £'+str(max_salary)+' Per Hour'

#         #General salary
#         else:
#             annual_salary = '£'+str(min_salary)+ ' - £'+str(max_salary)
                
#     except:
#          #Competative salary / Hidden salary
#             annual_salary = 'Competitive salary'

#     return annual_salary
