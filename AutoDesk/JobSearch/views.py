from django.shortcuts import redirect, render
from APIControl.views import ReedSearchAPI, LibrarySearchAPI


def Index(request):
    return redirect('HomePage:Index')

def Search(request,title,location,page_no):
     # === API CALLS === #
    Results = []
    Results.extend(LibrarySearchAPI(request,title,location,page_no))
    Results.extend(ReedSearchAPI(request,title,location,page_no))
    max_page = len(Results)

    #Template Context
    page_index = [page_no-1,page_no+1,page_no+2,page_no+3, max_page]
    searchParams ={'title':title, 'location':location, 'page_no':page_no, 'page_index':page_index, 'pagentation':False}
    context = {'Results': Results,'searchParams': searchParams}
    return render(request,'JobSearch/Results.html',context)






# ========== Job Lists ========== #

# jobList = []
# def JobList(request,title,location,page_no):

#     # === Total Jobs searches per page === #
#     jobList = []
#     maxPageLoad = 1

#     for pageLoad in range(maxPageLoad):
#         #Job Type
#         jobtype = title
#         joblocation = location
#         page = requests.get('https://www.reed.co.uk/jobs/'+jobtype+'pe-jobs-in-'+joblocation+'?pageno='+str(page_no))
#         soup = BeautifulSoup(page.text,'html.parser')

#         #search result find_all(params)
#         results = soup.find_all('article', class_ = 'job-result-card')


#         for jobs in results:
#             try:
#                 job_company_logo = jobs.img['data-src']
#                 job_company_logo = job_company_logo[:-15] 
#             except:
#                 job_company_logo = ''

#             job_id = jobs.get('id')
#             job_id = job_id.replace("jobSection", "") 

#             job_salary = jobs.find('li', class_ ='job-metadata__item--salary').text
#             job_salary = job_salary.split()[:3]
#             job_salary = ' '.join(job_salary)

#             job_posted = jobs.find('div', class_ ='job-result-heading__posted-by').text
#             job_posted = job_posted.split()[:3]
#             job_posted = ' '.join(job_posted)

#             job_entry = {
#             'job_title': jobs.find('h3', class_ = 'job-result-heading__title').find('a').text, 
#             'job_salary': job_salary,
#             'job_posted': job_posted,
#             'job_company': jobs.find('div', class_ ='job-result-heading__posted-by').find('a').text, 
#             'job_location': jobs.find('li', class_ ='job-metadata__item--location').text, 
#             'job_verified': False, 
#             'job_link': jobs.find("a").get('href'),
#             'job_id': job_id,
#             'job_company_logo': job_company_logo
#             }

#             #print(job_entry)

#             jobList.append(job_entry)
#             pageLoad += 1
#             page_no += 1
        

#     searchParams ={'title':title, 'location':location, 'page_no':page_no}
#     context = {
#         'jobList': jobList,
#         'searchParams': searchParams
#     }
#     return render(request,'JobSearch/JobsPage.html',context)



# ========== Job Page ========== #

# def JobPage(request,title,location,Id):
#     #Job Type
#     jobtype = title
#     joblocation = location
#     page = requests.get('https://www.reed.co.uk/jobs/fill/'+str(Id))
#     soup = BeautifulSoup(page.text,'html.parser')

#     results = soup.find('div', class_ ='col-lg-12')


#     job_posted = results.find('div', class_ ='posted').text
#     job_posted = job_posted.split()[:3]
#     job_posted = ' '.join(job_posted)


#     job_salary = results.find('div', class_ ='salary').text
#     job_salary = job_salary.split()[:3]
#     job_salary = ' '.join(job_salary)

#     job_description = results.find('div', class_ ='description')
#     job_description = job_description.find('span')
#     clear_spaces = ""
#     for elementshtml in job_description:
#         clear_spaces += str(elementshtml)
#     job_description = clear_spaces
#     #function to covert html

#     try:
#         job_company_logo = results.img['data-src']
#         job_company_logo = job_company_logo[:-15] 
#     except:
#         job_company_logo = ''


#     job_entry = {
#     'job_title': results.find('h1').text, 
#     'job_location': results.find('div', class_ ='location').text, 
#     'job_type': results.find('div', class_ ='time').text, 
#     'job_description': job_description,
#     'job_salary': job_salary,
#     'job_company_logo':job_company_logo,
#     'job_posted':job_posted,
#     'job_company': results.find('div', class_ ='posted').find('a').text, 
#     'job_link': 'https://www.reed.co.uk/jobs/fill/'+str(Id)
#     }
    
#     context = {'job': job_entry,}
#     return render(request,'JobSearch/FullJobsPage.html',context)


#useful code for future
        #show indented dict 
        # json_string = json.dumps(json_string, indent=4)
        # print('='*60)
        # print(json_string)
        # print(type(page))
        #print(page.content)

