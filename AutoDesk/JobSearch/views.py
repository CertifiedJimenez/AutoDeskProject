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
        job_entry = []
        job_title = jobs.find('h3', class_ = 'title').find('a').text # array 0
        job_salary = jobs.find('li', class_ ='salary').text # array 1
        job_salary = job_salary.split()[:3]
        job_salary = ' '.join(job_salary) 
        job_posted = jobs.find('div', class_ ='posted-by').text # array 2
        job_posted = job_posted.split()[:3]
        job_posted = ' '.join(job_posted)
        job_company = jobs.find('div', class_ ='posted-by').find('a').text # array 3
        job_location = jobs.find('li', class_ ='location').text # array 4
        job_verified = False # array 5


        try:
            job_company_logo = jobs.img['data-src']
            job_company_logo = job_company_logo[:-15]
        except:
            job_company_logo = 'N/A'



        job_entry = [job_title,job_salary,job_posted,job_company,job_location,job_verified,job_company_logo]
        jobList.append(job_entry)
        
    time.sleep(4)


    context = {
        'jobList': jobList
    }
    return render(request,'JobSearch/JobsPage.html',context)

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