# Portfolio Application

This Django application serves as a portfolio platform, allowing users to showcase their locations in Google Maps. It includes functionality for updating user profiles, displaying user details, managing user lists, retrieving user locations as JSON, and user redirection based on user type.

## Installation and Setup

Ensure you have latest Python installed on your system before proceeding.

1. Clone the repository:
- git clone https://github.com/Dilipsa/protfolio

2. Navigate to the project directory:
- cd portfolio

3. Create a virtual environment:
- On Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  python -m venv venv
  source venv/bin/activate
  ```

4. Install the required dependencies:
- pip install -r requirements.txt

5. Set up the database:
- python manage.py migrate

6. Create a `.env` file:
- Create a file named `.env` in the root directory of the project.
- Add the necessary environment variables to the `.env` file (refer to the `.env.example` file for the required variables).

7. Create a superuser:
- python manage.py createsuperuser

8. Start the development server:
- python manage.py runserver

9. Access the application at [http://localhost:8000](http://localhost:8000).

10. In the Navbar, click the `Register` link.

11. Register a user using an email address.

12. Update the profile by clicking the `Profile` link in the navbar after logging in.

13. Log out and log in again as a superuser to view all users on the Google Map.

Ensure you have Python and Django installed on your system before proceeding.

## Functionality

### UserProfileView

- URL: `/user/profile/`
- Method: GET, POST
- Description: This view allows authenticated users to update their profile information.
- Template: `users/user_profile.html`
- Form: `ProfileUpdateForm`
- Success URL: `users:user_details`

### UserDetailsView

- URL: `/user/details/<pk>/`
- Method: GET
- Description: This view retrieves the user object with the given primary key (pk) and renders the user details page.
- Template: `users/user_details.html`
- Context Variable: `user`

### user_lists

- URL: `/user/lists/`
- Method: GET
- Description: This view renders all users in Google Maps and is only accessible to superusers.
- Template: `users/user_lists.html`

Note: Users have to update latitude and longitude values for their location to be visible on the map.

### UserRedirectView

- URL: `/user/redirect/`
- Method: GET
- Description: This view redirects the user to a specific URL based on their user type.
- Redirection: If the user is a superuser, they are redirected to `users:user_lists`. Otherwise, they are redirected to `users:user_profile`.
