from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View


# Create your views here.
class AboutView(View):
    def get(self,request):
        data = {
            "ID"            : 1,
            "Full_name"    : "Lulu Farhan",
            "title"        : "Python Django React Fullstack intern",
            "bio"          : "A passionate developer building scalable applications.",
            "DOB"          : "08/06/2001",
            "email"        : "lulufarhan8086gmail.com",
            "contact"      : 8086088631,
            "location"     : "Kozhikode",
            "Github_URL"   : "https://github.com/Lulufarhann08",
            "LinkedIn_URL" : "https://www.linkedin.com/in/lulu-farhan-a3764b331"
            }
        return JsonResponse(data)
    
class EducationView(View):
    def get(self,request):
        data = {
            "ID"             : "WYD22CS038",
            "institution"    : "Government Engineering College Wayanad",
            "course"         : "Computer Science Engineering",
            "university"     : "KTU University",
            "location"       : "Mananthavady",
            "Starting_year"  : "2022",
            "Ending_year"    : "2026",
            "cgpa "          : "7",
            "description"    : "Completed Btech Computer Science Engineering"
            
        }
        return JsonResponse(data)
class ProjectView(View):
    def get(self,request):
        projects = [
            {
                "id" : "1",
                "title": "Blood Donor Management",
                "short_description": "Managing Donors, Donations, and Blood Requests",
                "long_description" : 'A system that manages blood donors and requests, helping hospitals and patients find available donors by blood group and location.',
                "technologies_used" : ["Python", "Streamlit", "MySQL"],
                "live_url" : 'http://localhost:8501',
                "github_url" : "https://github.com/Lulufarhann08/Blood-Donor-Management-System",
                "featured" : "true"
            },
            {
               "id" : "2",
                "title": "Gym Management System",
                "short_description": "Managing Gym Members and Memberships",
                "long_description" : 'A Gym Management System built with Python, Streamlit, and MySQL to manage members, memberships, attendance, and payments.',
                "technologies_used" : ["Python", "Streamlit", "MySQL"],
                "live_url" : 'http://localhost:8501',
                "github_url" : "https://github.com/Lulufarhann08/Gym-Member-Management-System",
                "featured" : "true" 
            }
        ]
        
        return JsonResponse(projects, safe=False)
    
class SkillView(View):
    def get(self,request):
        skills = [
                {
                "id": 1,
                "skill_name": "Python",
                "category": "Programming Language",
                "proficiency": "Advanced",
                "years_of_experience": 1 
                },
               {
               "id": 2,
               "skill_name": "C",
               "category": "Programming Language",
               "proficiency": "Intermediate",
               "years_of_experience": 4
               }, 
            {
                "id": 3,
                "skill_name": "Java",
                "category": "Programming Language",
                "proficiency": "Beginner to intermediate",
                "years_of_experience": 3 
                },                            
               {
               "id": 4,
               "skill_name": "Django",
               "category": "Backend",
               "proficiency": "Intermediate",
               "years_of_experience": 0
               },
               {
              "id": 5,
              "skill_name": "SQL",
              "category": "Database",
              "proficiency": "Advanced",
              "years_of_experience": 2
              },
                {
                "id": 6,
               "skill_name": "HTML",
                "category": "Web developement",
                "proficiency": "Intermediate",
                "years_of_experience": 1
                },
                {
                "id": 7,
               "skill_name": "CSS",
                "category": "Web developement",
                "proficiency": "Beginner to intermediate",
                "years_of_experience": 1
                },
                {
                 "id": 8,
                "skill_name": "Javascript",
                 "category": "Web developement",
                 "proficiency": "Beginner to intermediate",
                 "years_of_experience": 1
                 },
                                                    
        ]
        return JsonResponse(skills, safe=False)