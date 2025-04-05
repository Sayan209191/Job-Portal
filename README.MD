# Job Portal Project

## Overview

This is a **Job Portal** web application built using **Django** and **MySQL**. It allows users to search for jobs, internships, and companies based on various filters. The portal also provides search suggestions and pagination for better user experience.

## Features

- **User Authentication:** Signup/Login using Django Auth and Google OAuth.
- **Job & Internship Listings:** View and filter job/internship postings by title, company, skills, and location.
- **Company Profiles:** Search and view company descriptions.
- **Search Functionality:**
  - **Live search suggestions** for jobs and companies.
  - **Redirects to company pages** if a company is searched.
- **Pagination:** Implemented for jobs and search results.
- **Admin Panel:** Managed using **Django Grappelli**.

## Technologies Used

- **Backend:** Django, MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Django Auth, Google OAuth
- **Deployment:** TBD

## Setup Instructions

### Prerequisites

- Python 3.x
- Virtual Environment (optional but recommended)
- MySQL Database

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sayan209191/Job-Portal.git
   cd job-portal
   ```

2. **Create a Virtual Environment & Activate it**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL**

   - Update `settings.py` with your **MySQL** database credentials.

5. **Run Migrations & Start Server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

6. **Access the Application**

   - Open `http://127.0.0.1:8000/` in your browser.

## Folder Structure

```
JOBPORTAL/
│-- accounts/              # User authentication
│-- jobportal/             # Main Django project folder
│-- jobs/                  # Job-related features
|-- blog/                  # Blog/Article feature
│-- media/                 # Uploaded images/files
│-- myapp/                 # Additional Helper app 
│-- static/                # Static files (CSS, JS, Images)
│-- template/              # HTML templates
│-- manage.py              # Django management script
│-- .gitignore             # Git ignore file
```

## API Endpoints

| Endpoint               | Method | Description                   |
| ---------------------- | ------ | ----------------------------- |
| `/search`              | GET    | Search for jobs and companies |
| `/search-suggestions/` | GET    | Fetch live search suggestions |
| `/auth/signup`         | POST   | User Signup                   |
| `/auth/login`          | POST   | User Login                    |
| `/company/<id>`        | GET    | View company profile          |
|`/blog/`                |  GET   |    View blog list             |
|`/blog/create/`         | POST   |  Create a new blog post       |

## To-Do / Future Enhancements

- **Job Apply Feature**: Allow users to apply directly.
- **Admin Panel Enhancements**: More job posting controls.
- **Better UI/UX Improvements**.

## Contributors

- **Sayan Ghorui** 
- **Chinmay Khanra** 
- **Chayan Samanta** 

## License

This project is licensed under the **MIT License**.

---

**Happy Coding! 🚀**

