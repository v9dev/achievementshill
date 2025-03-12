# Achievements Hill

Achievements Hill is a full-stack web application that enables users to create and share their achievements. Built using Flask and Cloudinary for media storage.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Future Plans](#future-plans)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication**: Secure sign-up and login functionality.
- **Profile Management**: Users can create and edit personal profiles.
- **Achievement Creation**: Add new achievements with titles, descriptions, and images.
- **Achievement Sharing**: Share achievements with others via unique links.
- **Cloudinary Storage**: Store and manage images efficiently using Cloudinary.
- **Responsive Design**: Optimized for various devices, including desktops and mobile devices.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Database**: Firebase Realtime Database
- **Authentication**: Firebase Authentication
- **Storage**: Cloudinary (Replacing Firebase Storage)

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/v9dev/achievementshill.git
   cd achievementshill
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set Up Firebase Authentication & Database**:
   Create a `.env` file in the project root directory and add your Firebase configuration details:
   ```env
   FIREBASE_API_KEY='Your Api Key'
   FIREBASE_AUTH_DOMAIN='Your Auth Domain'
   FIREBASE_DATABASE_URL='Your Database URL'
   FIREBASE_PROJECT_ID='Your Project ID'
   FIREBASE_MESSAGING_ID='Your Messaging ID'
   FIREBASE_APP_ID='Your App ID'
   FIREBASE_MEASUREMENT_ID='Your Measurement ID'
   ```

2. **Set Up Cloudinary for Media Storage**:
   Sign up at [Cloudinary](https://cloudinary.com/) and get your API credentials. Then, add the following to your `.env` file:
   ```env
   CLOUDINARY_CLOUD_NAME='your_cloud_name'
   CLOUDINARY_API_KEY='your_api_key'
   CLOUDINARY_API_SECRET='your_api_secret'
   ```

## Usage

1. **Run Database Migrations**:
   ```bash
   python migration.py
   ```

2. **Run the Application**:
   ```bash
   flask run
   ```

3. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

4. **Upload Images to Cloudinary**:
   - When adding an achievement, images will be uploaded to Cloudinary instead of Firebase Storage.
   - Ensure your Cloudinary API credentials are correctly set in the `.env` file.

## Screenshots

### Home Page
![home page](https://user-images.githubusercontent.com/99959044/216848948-e6eba65d-9972-4df2-93bb-04c38a90e434.PNG)

### Login Page
![Login](https://user-images.githubusercontent.com/99959044/216848960-78aed3a0-7920-44ef-9edb-5f0099a19e65.PNG)

### Sign Up Page
![signup](https://user-images.githubusercontent.com/99959044/216848968-a5c23040-8c27-445a-b156-ff1ef648f69b.PNG)

## Achivement Page
![View Page](https://user-images.githubusercontent.com/99959044/216848995-a1c769af-d431-4aa8-b0f0-2eabb48fe5a9.PNG)

## Edit Achivement Page
![edit  achivement Page](https://user-images.githubusercontent.com/99959044/216849021-b62a144a-5db2-4d65-84f5-74b79e645e4a.PNG)

## Edit Profile
![edit profile page](https://user-images.githubusercontent.com/99959044/216849026-4670d1dc-dc16-4af9-bed8-f22cd0969453.PNG)

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**:
   - Click the "Fork" button at the top right corner of this page.

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/your-username/achievementshill.git
   cd achievementshill
   ```

3. **Create a New Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**:
   - Implement your feature or fix.

5. **Commit Your Changes**:
   ```bash
   git add .
   git commit -m "Add feature: your feature name"
   ```

6. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**:
   - Navigate to the original repository and click on "Pull Requests".
   - Click "New Pull Request" and select your branch.

## Future Plans

We have several exciting features planned for future updates:

- **Filters**: Improve searching and filtering of achievements.
- **Discussion Groups**: Create groups where users can discuss achievements.
- **Friends System**: Add a feature to connect and interact with friends.
- **Voting System**: Allow users to vote on achievements.
- **Achievement Badges**: Introduce badge rewards for user achievements.
- **New UI Elements**: Enhance the user interface with a modern design.
- **Modular Flask Architecture**: Refactor the codebase using Flask Blueprints.
- **Cloud Deployment**: 
  - Utilize Docker for containerization.
  - Implement AWS services for scalable hosting.
  - Integrate GitHub Actions for automated CI/CD workflows.
- **Additional Features**: More enhancements and functionalities to be added in the future!

⭐ **Star this repository** to stay updated on upcoming features!

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/v9dev/achievementshill/blob/main/LICENSE) file for details.

## Contact

For questions or suggestions, please open an issue in this repository.
