#  Sober Spaces – Django Blog Platform
---
**Sober Spaces** is a full-stack blog web application built using Django. It allows users to create, read, update and delete (CRUD) posts about sobriety journeys and alcohol-free venues. This project was developed as part of the Level 5 Diploma in Web Application Development, Unit 3: Back End Development.

---
## Live Site

This project is deployed on Heroku and can be accessed here:

[View the Live Site: Sober Spaces](https://ms3-blog-17789f37c9f8.herokuapp.com/)

## Admin Panel Access

This Django application includes an admin panel for managing posts, categories, and user comments.

You can access the admin interface here:

[Admin Panel](https://ms3-blog-17789f37c9f8.herokuapp.com/admin/login/?next=/admin/)

### Superuser Credentials (for testing)

These credentials are only for project assessment and testing purposes.

- **Username:** `sarashipley`
- **Password:** `123`


## Table of Contents

- [Purpose & Target Audience](#purpose--target-audience)
- [User Stories](#user-stories)
- [Features](#features)
- [Project Management](#project-management)
- [Database Schema](#database_schema)
- [Entity Relationship Diagram](#entity-relationship-diagram-erd)
- [UX & Accessibility Design](#ux--accessibility-design)
- [Data Model](#data-model)
- [Validation & Accessibility Testing](#validation--accessibility-testing)
- [Future Improvements](#future-improvements)
- [Clean Code & Development Standards](#clean-code--development-standards)
- [Manual Testing](#manual-testing)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Security](#security)
- [Custom Error Pages](#custom-error-pages)
- [Code Quality](#code-quality)
- [Lessons Learned](#lessons-learned)
- [Project Structure](#project-structure)
- [Acknowledgements](#acknowledgements)

---


## Purpose & Target Audience

This project serves a community of users who are interested in living alcohol-free lifestyles and wish to share experiences, recommend venues, and find inspiration through blog content. It’s designed to be simple, intuitive and accessible.

---

## User Stories

**As a visitor, I want to:**

- Browse recent blog posts  
- Filter posts by category  
- Read inspiring stories from others  
- View featured content  

**As a registered user, I want to:**

- Sign up and log in securely  
- Create new blog posts  
- Upload an image with each post  
- Edit or delete my own posts  
- See feedback when my actions succeed or fail  

**As an admin, I want to:**

- View and delete comments from admin panel if nessesary
- Manage categories from the admin panel  
- Ensure platform security and data integrity  

> **INCLUDE SCREENSHOTS HERE!**
---

## Features

- User registration & login/logout (Django Allauth)  
- Create, edit & delete posts (authenticated users only)  
- Categorised post filtering  
- Featured "latest" post highlighted at the top  
- Image upload per post  
- Comment system 
- Pagination for performance and UX  
- Responsive layout with Bootstrap 5.3  
- Custom CSS theme (clean, accessible, and consistent)  
- Deployed to Heroku with PostgreSQL database  

---

## Project Management/Agile Delivery

Project planning and task tracking were managed using the GitHub Projects board. The board was structured using columns **To Do**, **In Progress**, and **Done** to organise tasks effectively and ensure steady progress throughout development.

Each issue or task was broken down into manageable items, including UI design, CRUD functionality, testing, and deployment.

![GitHub Project Board Screenshot](https://github.com/user-attachments/assets/9f06527c-3ecd-4f42-82c7-a2a23da46a8d)

## Entity Relationship Diagram (ERD)

The ERD was especially useful in:
- Identifying how posts and comments are tied to users
- Structuring the `Post` model with foreign keys to both `User` and `Category`
- Clarifying the 1-to-many relationships between `User → Post`, `User → Comment`, and `Post → Comment`
- Removing unnecessary complexity (e.g., a custom `Profile` model)

The diagram below illustrates the final data structure used in the app:

<img src="docs/images/erd.png" alt="Blog ERD" width="500"/>

[Download ERD (PNG)](docs/images/erd.png)

## Database Schema

The diagram below shows how the main parts of the website's data are connected. Each blog post is written by a registered user and can belong to a category (like "Health" or “Travel”). Users can also leave comments on posts. Each comment is linked both to the post it’s about and to the user who wrote it. This structure keeps everything organised and makes it easy to manage content and users within the site.

<img src="docs/images/database_schema.png" alt="Database Schema" width="1000"/>



## UX & Accessibility Design

- Built with UX principles: clear navigation, visible feedback, and form validation  
- Follows accessibility standards: readable fonts, clear contrast, semantic HTML  
- Fully responsive (mobile-first)  
- Navigation supports keyboard and screen readers  
- Feedback messages on key actions (e.g. post created, login failed)  

[View wireframes and design rationale on Figma](https://www.figma.com/) *ADD LINK HERE!!*

---

## Data Model

### Post

| Field      | Type          | Notes                    |
|------------|---------------|--------------------------|
| title      | CharField     | Required, max_length=100 |
| content    | TextField     | Required                 |
| image      | ImageField    | Optional                 |
| author     | FK → User     | Required                 |
| category   | FK → Category | Optional                 |
| created_at | DateTimeField | auto_now_add             |
| updated    | DateTimeField | auto_now                 |

### Category

| Field | Type      | Notes            |
|-------|-----------|------------------|
| name  | CharField | Required, unique |

### Comment

| Field | Type         | Notes          |
|-------|--------------|----------------|
| post  | FK → Post    | Required       |
| name  | CharField    | Required       |
| email | EmailField   | Required       |
| body  | TextField    | Required       |
| active| BooleanField | For moderation |

---

## Manual Testing

| Test Case                    | Expected Outcome                               | Result   |
|-----------------------------|------------------------------------------------|----------|
| Register new user           | Redirects with success message                 | ✅ Pass  |
| Login                       | Authenticated user dashboard shown             | ✅ Pass  |
| Create/Edit/Delete post     | Data updates appear correctly on frontend      | ✅ Pass  |
| Post pagination             | Older posts accessible                         | ✅ Pass  |
| Filter by category          | Filter works as expected                       | ✅ Pass  |
| Image upload                | Displays on homepage and detail view           | ✅ Pass  |
| Commenting                  | Comments added with CRUD                       | ✅ Pass  |
| Responsive layout           | Works on mobile, tablet, desktop               | ✅ Pass  |
| 404 pages                   | Custom error page loads                        | ✅ Pass  |
| Static files                | CSS and JS load correctly                      | ✅ Pass  |

- See full bug documentation in [BUG_FIX_REPORT.md](BUG_FIX_REPORT.md) *ADD LINK HERE!!*


---

## Technologies Used

- Python 3.13  
- Django 4.2  
- PostgreSQL  
- Heroku  
- Bootstrap 5.3  
- Django Allauth  
- Cloudinary (image uploads)  
- HTML5, CSS3  

---

## Deployment

**Deployed on Heroku**

### Steps:

1. Set up PostgreSQL on Heroku  
2. Added environment variables  
3. Installed production dependencies: Gunicorn, Psycopg2  
4. Ran `python manage.py collectstatic`  
5. Connected Heroku to GitHub for auto-deploy  

---

## Security

- `.env` file stores secrets and is not committed  
- `DEBUG = False` in production  
- `ALLOWED_HOSTS` and CORS configured  
- Admin access restricted to superusers  
- Login required for editing/deleting posts  

---

## Custom Error Pages

The application includes custom error pages for 403, 404, and 500 errors. These help ensure users are guided when something goes wrong, instead of seeing a browser or Django error screen.

The `404.html` file is implemented as a standalone HTML page to avoid potential rendering issues during production when `DEBUG = False`. This ensures stable and user-friendly error feedback.

This approach meets the specification’s requirement for robust error handling and clear user messaging.

---

## Code Quality

- Python code follows PEP8  
- HTML/CSS validated with W3C and Jigsaw  
- Git used with descriptive commits  
- Clean file structure and naming conventions  
- Code comments added where needed  

---

##  Clean Code & Development Standards

- **Naming Conventions**  
  - Descriptive and consistent naming across files, functions, and variables  
  - All lowercase file names with no spaces for cross-platform compatibility  

- **File Structure**  
  - Templates, static files, and media are grouped by type  
  - Custom code is separated from third-party libraries  

- **Code Readability**  
  - Code is consistently indented and spaced  
  - Clear comments are provided for all custom logic  
  - Semantic HTML is used for proper structure  
  - HTML, CSS, and Python files are kept separate  

- **Defensive Design**  
  - Form inputs include backend validation (required fields, types, etc.)  
  - Authentication enforced for actions like post creation and deletion  
  - Custom 404 pages and feedback messages improve user experience  

- **Compliant & Robust Code**  
  - HTML validated via [W3C](https://validator.w3.org/)  
  - CSS validated via [Jigsaw](https://jigsaw.w3.org/css-validator/)  
  - Python code conforms to [PEP8](https://peps.python.org/pep-0008/)  
  - JS (where used) tested using [JSHint](https://jshint.com/)  
  - Logic errors tested manually and addressed  
  - Input and upload errors handled gracefully  

This approach ensures the application is readable, scalable, accessible and robust for real users.

---


##  Validation & Accessibility Testing

[Read testing report.md](testing.md)

- **HTML Validation**: All HTML templates were passed through [W3C Validator](https://validator.w3.org/) and fixed for any structural issues.
- **CSS Validation**: Stylesheets were tested using [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) with no major warnings.
- **Python Code Quality**: Code conforms to [PEP8](https://peps.python.org/pep-0008/) using `flake8` and VSCode extensions. 
- **Lighthouse Testing**:
  - **Performance**: 
  - **Accessibility**: 
  - **Best Practices**: 
  - **SEO**: 
- **Keyboard Navigation**: All interactive elements are reachable and operable using Tab and Enter keys.
- **Screen Reader Compatibility**: Tested using VoiceOver on Mac. Headings, landmarks, and buttons are accessible.
- **ARIA Labels**: Not required due to semantic markup but included where helpful.

---

## Future Improvements

**Comment Moderation**

Comment moderation was considered during development to allow admin approval before displaying user-submitted comments. However, to streamline the user experience and simplify testing, moderation was omitted in the current version. Comments are displayed immediately upon submission.

This decision allowed for a clearer focus on core CRUD functionality and user interaction. If time permits, moderation may be reintroduced as an enhancement by enabling the existing `active` field and filtering comments accordingly.

---

##  Lessons Learned

- ImageField requires proper config (MEDIA settings, Pillow)  
- Always test for image path and field name accuracy  
- Separate user vs admin access clearly  
- Test all edge cases during development  
- Make use of Figma or paper wireframes before starting  

---

##  Project Structure



---

##  Acknowledgements

- Django Docs  
- Bootstrap Docs  
- Cloudinary Docs  
- Code Institute examples and course materials for gudiance and inspiration  
- Blog post content generated by AI
- Unsplash for images
- Drawsql was used for database schema
- Django 5 By Example by Antonio Mele was used as a point of reference
- Matt Rudge youtube tutorials for a guidance
- Special thanks to Spencer Bariball for this help and guidance on this project

