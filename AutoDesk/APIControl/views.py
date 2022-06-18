from ast import keyword
import requests
from requests.auth import HTTPBasicAuth
from DataHandler.views import Job_Salary, Job_Posted, Job_Logo

# Create your views here.
reed_api_key = 'aa04a771-9788-4d0b-bb72-44b7d5d2f234'
google_api_key = 'AIzaSyAXPnajPyEx-ONCY_r6zIXW1HPNs5TNcLs'
cv_library_api_key = 'hqMwEXhPBMfFqerp'

# ==== API Functions Reed, Goolgle Maps  ====#

saved_location = []
def getGeoLocation(request,location):
    #singe world strong filter
    if len(location.split()) == 1:
        location = f'United Kingdom {location}'
    location = location.replace(' ', '%20')

    #Prevents any slowdowns and repeat API calls
    if any(location in sublist for sublist in saved_location):
        i = 0
        for findlocation in saved_location:
            if location == findlocation[0]:
                latitude = findlocation[1]
                longitude = findlocation[2]
                return latitude, longitude
    else:
        #API call
        googleMaps = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={google_api_key}')
        googleMaps = googleMaps.json()
        googleMaps = googleMaps['results']
        
        #formatting
        latitude = 0
        longitude = 0
        for data in googleMaps:
            #Filters to lat, lng dictionary
            data = data['geometry']
            data = data['location']
            latitude = data['lat']
            longitude = data['lng']
            saved_location_value = [location,latitude,longitude] 
        # saved_location.append(saved_location_value)
        return latitude, longitude

def ReedSearchAPI(request,title,location,page_no):
    url_extension = ""

    #Search conditions
    keywords = title
    locationName = location
    versionnumber = 1.0
    postedByDirectEmployer = False
    fullTime = True
    distanceFromLocation = 5

    #Filter options
    # if request.method == 'POST':
    #     valid = request.POST.get('data[valid]')
    #     Salary = [request.POST.get('data[MinimumRange]'),request.POST.get('data[MaximumRange]')]
    #     url_extension = f'&minimumSalary={Salary[0]}&maximumSalary={Salary[1]}'
    

    #allows for URL filteration
    url = f'https://www.reed.co.uk/api/{versionnumber}/search?keywords={keywords}&locationName={locationName}&distanceFromLocation={distanceFromLocation}&fullTime={fullTime}&page={page_no}'+url_extension
    page = requests.get(url,auth=HTTPBasicAuth(reed_api_key,'password'))

    #turn to JSON & API Context
    page = page.json()
    max_page = page['totalResults']    
    page = page['results']

    jobList = []
    for job in page:
        job_entry = {
        'job_title': job['jobTitle'],
        'job_urlpath': 1,
        'job_salary': Job_Salary(request,job,1),
        'job_posted': Job_Posted(job['date']),
        'job_company': job['employerName'],
        'job_location': job['locationName'],
        'job_verified': False,
        'job_link': job['jobUrl'],
        'job_id':job['jobId'],
        'job_company_logo': Job_Logo(job),
        'coordinates': getGeoLocation(request,job['locationName'])
        }
        jobList.append(job_entry)
    return jobList

def LibrarySearchAPI(request,title,location,page_no):
    url_extension = ""

    #Search conditions
    keywords = title
    locationName = location
    Key = cv_library_api_key

    #allows for URL filteration
    url = f'https://www.cv-library.co.uk/search-jobs-json?key={Key}&q={keywords}&geo={locationName}&distance=15&salarytype=annum'
    page = requests.get(url,auth=HTTPBasicAuth(reed_api_key,'password'))

    #turn to JSON & API Context
    page = page.json()
    max_page = page['total_entries']   
    page = page['jobs']
 
    jobList = []
    for job in page:
        try:
            Salary = Job_Salary(request,job['salary'],2)
        except:
            Salary = "Competative"

        job_entry = {
        'job_title': job['title'],
        'job_urlpath': 2,
        'job_salary': Salary,
        'job_posted': Job_Posted(job['posted']),
        'job_company': job['agency']['title'],
        'job_location': job['location'],
        'job_verified': False,
        'job_link': '',
        'job_id':job['id'],
        'job_company_logo': Job_Logo(job),
        'coordinates': getGeoLocation(request,job['location'])
        }
        jobList.append(job_entry)
    return jobList

def ReedDetailsAPI(request,Id):
    JobId = Id
    versionnumber = 1.0
    url = f'https://www.reed.co.uk/api/{versionnumber}/jobs/{JobId}'
    page = requests.get(url,auth=HTTPBasicAuth(reed_api_key,'password'))
    page = page.json()

    job_entry = {
    'job_title': page['jobTitle'], 
    'job_location': page['locationName'], 
    'job_type': page['contractType'], 
    'job_description': page['jobDescription'],
    'job_salary': Job_Salary(request,page,1),
    'job_company_logo': Job_Logo(),
    'job_posted': Job_Posted(request,page['datePosted']),
    'job_company': page['employerName'], 
    'job_link': page['jobUrl'],
    'coordinates': getGeoLocation(request,page['locationName'])
    }
    return job_entry

def LibraryDetailsAPI(request,Id):
    Key = cv_library_api_key
    keywords = Id
    url = f'https://www.cv-library.co.uk/search-jobs-json?key={Key}&q={keywords}'
    page = requests.get(url,auth=HTTPBasicAuth(reed_api_key,'password'))
    page = page.json()
    page = page['jobs'][0]
 
    
    try:
        Salary = Job_Salary(request,page['salary'],2)
    except:
        Salary = "Competative"
#=======================#

    job_entry = {
    'job_title': page['title'], 
    'job_location': page['location'], 
    'job_type': page['type'], 
    'job_description': page['description'],
    'job_salary': 'none',
    'job_company_logo': Job_Logo(page),
    'job_posted': Job_Posted(page['date']),
    'job_company': page['agency']['title'], 
    'job_link': page['url'],
    'coordinates': getGeoLocation(request,page['location'])
    }
    return job_entry