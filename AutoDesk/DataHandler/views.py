from datetime import datetime


# Create your views here.
def Job_Salary(request,job,config):
    annual_salary = ""
    min_salary = None

    #Identification Phase 
    match config:
        case 1:
            min_salary = job['minimumSalary']
            max_salary = job['maximumSalary']

        case 2:
            
            #Timeframe Payroll
            if '/hour' in job:
                hourly = True
            if '/annum' in job:
                hourly = False

            #Great Filter
            salary_list = []
            for item in job.split():
                numeric_filter = filter(str.isdigit, item)
                item = "".join(numeric_filter)
                if (item != ""):
                    if hourly == True:
                        item = float(item)/100
                    salary_list.append(item)
            job = salary_list

            match len(job):
                case 1:
                    min_salary = job[0]
                    max_salary = job[0]
                case 2:
                    min_salary = job[1]
                    max_salary = job[0]


        case _:
            annual_salary = 'Competitive salary'


    #Formatting Phase
    try:
        #remove .00 from salary


        #Min and max dymanics
        min_salary = int(min_salary)   
        max_salary = int(max_salary)   
        min_salary = "{:,}".format(min_salary)
        max_salary = "{:,}".format(max_salary)

        #Per Hour
        if len(str(min_salary)) <= 2:
            annual_salary = '£'+str(min_salary)+ ' - £'+str(max_salary)+' Per Hour'

        #General salary
        else:
            annual_salary = '£'+str(min_salary)+ ' - £'+str(max_salary)
                
    except:
         #Competative salary / Hidden salary
            annual_salary = 'Competitive salary'

    return annual_salary

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

