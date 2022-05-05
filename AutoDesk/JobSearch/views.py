from django.shortcuts import redirect, render
import requests
from bs4 import BeautifulSoup 
import time

# Create your views here.
def index(request):
    #Lazy Redirect
    return redirect('JobSearch:Search')

def Search(request):
    return render(request,'JobSearch/SearchPage.html')



jobList = []
def JobList(request,title,location):

    #Job Type
    jobtype = title
    joblocation = location
    page = requests.get('https://www.reed.co.uk/jobs/'+jobtype+'pe-jobs-in-'+joblocation)
    soup = BeautifulSoup(page.text,'html.parser')

    #search result find_all(params)
    results = soup.find_all('article', class_ = 'job-result')

    jobList = []
    for jobs in results:

        try:
            job_company_logo = jobs.img['data-src']
            job_company_logo = job_company_logo[:-15] 
        except:
            job_company_logo = ''

        job_id = jobs.get('id')
        job_id = job_id.replace("jobSection", "") 

        job_salary = jobs.find('li', class_ ='salary').text
        job_salary = job_salary.split()[:3]
        job_salary = ' '.join(job_salary)

        job_posted = jobs.find('div', class_ ='posted-by').text
        job_posted = job_posted.split()[:3]
        job_posted = ' '.join(job_posted)

        job_entry = {
        'job_title': jobs.find('h3', class_ = 'title').find('a').text, 
        'job_salary': job_salary,
        'job_posted': job_posted,
        'job_company': jobs.find('div', class_ ='posted-by').find('a').text, 
        'job_location': jobs.find('li', class_ ='location').text, 
        'job_verified': False, 
        'job_link': jobs.find("a").get('href'),
        'job_id': job_id,
        'job_company_logo': job_company_logo
        }

        #print(job_entry)

        jobList.append(job_entry)
        
        if len(jobList) >= 5:
            break

    
    searchParams ={'title':title, 'location':location}
    context = {
        'jobList': jobList,
        'searchParams': searchParams
    }
    return render(request,'JobSearch/JobsPage.html',context)



def JobPage(request,title,location,Id):

    #Job Type
    jobtype = title
    joblocation = location
    page = requests.get('https://www.reed.co.uk/jobs/fill/'+str(Id))
    soup = BeautifulSoup(page.text,'html.parser')

    results = soup.find('div', class_ ='col-lg-12')


    job_posted = results.find('div', class_ ='posted').text
    job_posted = job_posted.split()[:3]
    job_posted = ' '.join(job_posted)


    job_salary = results.find('div', class_ ='salary').text
    job_salary = job_salary.split()[:3]
    job_salary = ' '.join(job_salary)

    try:
        job_company_logo = results.img['data-src']
        job_company_logo = job_company_logo[:-15] 
    except:
        job_company_logo = ''


    job_entry = {
    'job_title': results.find('h1').text, 
    'job_location': results.find('div', class_ ='location').text, 
    'job_type': results.find('div', class_ ='time').text, 
    'job_description': results.find('div', class_ ='description').text,
    'job_salary': job_salary,
    'job_company_logo':job_company_logo,
    'job_posted':job_posted,
    'job_company': results.find('div', class_ ='posted').find('a').text, 
    'job_link': 'https://www.reed.co.uk/jobs/fill/'+str(Id)
    }

    print(job_entry)

    
    context = {'job': job_entry,}
    return render(request,'JobSearch/FullJobsPage.html',context)














#==========webscrape fetch==============
    # #Job Type
    # jobtype = 'Programmer'
    # page = requests.get('https://uk.indeed.com/jobs?q='+jobtype)
    # soup = BeautifulSoup(page.text,'html.parser')

    # #search result find_all(params)
    # results = soup.find_all('li')

    # jobList = []
    # for jobs in results:

    #     try:
    #         job_title = jobs.find('h2', class_ = 'jobTitle').text
    #         job_company = jobs.find('span', class_ ='companyName').text
    #         job_location = jobs.find('div', class_ ='companyLocation').text
    #         job_salary = jobs.find('div', class_ ='salary-snippet').text
    #         job_posted = jobs.find('span', class_ ='date').text
    #         jobList.append(job_title)
            
    #     except:
    #         jobList.append('loss')

    # jobList.append(job_title,job_company,job_location,job_salary,job_posted)