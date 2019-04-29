
from bs4 import BeautifulSoup
import re
import json


def glassdoor_list(soup):   
    #extract company name
    company = soup.find_all("p","employerName")[0].get_text()
    

    #extract job title 
    jobtitle = soup.find_all("h1","jobTitle")[0].get_text()

    #extract job description
    jobdescription = soup.find_all("div","jobDescriptionContent desc")[0].get_text()
    #print("Glassdoor : Job title {1} | Company {2} | Job description {0}". format(jobdescription, jobtitle, company))
    return company.strip(), jobtitle.strip(), jobdescription.strip()

def linkedin_list(soup):
    #extract company name
    company = soup.body.findAll("a","jobs-details-top-card__company-url ember-view")[0].get_text()

    #extract job title 
    jobtitle = soup.body.findAll("div","jobs-details-top-card__content-container mt6 pb5")[0].findAll("h1","jobs-details-top-card__job-title t-20 t-black t-normal")[0].get_text()

    #extract job description
    jobdescription = soup.body.findAll("article")[0].get_text()
    #print("Linkedin_main : Job title {1} | Company {2} | Job description {0}". format(jobdescription, jobtitle, company))
    return company.strip(), jobtitle.strip(), jobdescription.strip()


def linkedin_main(soup):
    title = soup.head.title.get_text().split("|")

    #extract company name
    company = title[1]

    #extract job title 
    jobtitle = title[0]

    #extract job description
    jobdescription = soup.body.findAll(id="job-details")[0].get_text()
    #print("Linkedin_main : Job title {1} | Company {2} | Job description {0}". format(jobdescription, jobtitle, company))
    return company.strip(), jobtitle.strip(), jobdescription.strip()


def extract_text(fp):
    #find linkedin (listing vs main)/ glassdoor(listing)
    soup = BeautifulSoup(fp,'html.parser')
    title = soup.head.title.get_text().split("|")
    
    if " Glassdoor" in title:
        return glassdoor_list(soup)

    if " LinkedIn" in title:
        
        #linkedin listing view
        if len(title) == 2:
            return linkedin_list(soup)
        
        #linked main view
        else:
            return linkedin_main(soup)

    return


if __name__=="main":
###get the html
    with open("data/test_glass.html",encoding="utf8") as fp:
        soup = BeautifulSoup(fp)

    company, jobtitle, jobdescription = extract_text(soup)

    print(company, jobtitle, jobdescription)




