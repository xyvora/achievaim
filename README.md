# Achiev𝘼𝙄m

| Link | Description |
|:-----|:------------|
| [achievaim repo](https://github.com/xyvora/achievaim) | Codebase |
| [Achiev𝘼𝙄m Project](https://github.com/orgs/xyvora/projects/1) | Project progression, tracking and management. |
| [Achiev𝘼𝙄m Wiki](https://github.com/xyvora/achievaim/wiki) | Past meeting notes, research, and documentation. |
| [Achiev𝘼𝙄m Discord Conversation](https://discord.gg/n3CDBbWw) | Achiev𝘼𝙄m discussions on development, help and ideas. 

---
Achiev𝘼𝙄m is a user-friendly and scalable SaaS web application. It seamlessly integrates with calendar and other software applications, leveraging the power of Generative AI to assist users in creating and tracking their SMART goals effectively.

---
## Features

- Identify and create SMART goals using a click of a button.
- Generate personalized goal suggestions using OpenAI GPT API
- Track goal progress and update details from a single page
- Set goal duration, days of the week, and repetition
- Easily integrate SMART goals with automatic SMART goal events in Google or Outlook.

---
## Tech Stack

- Svelte: Front-end framework for building user interfaces
- Tailwind CSS: Utility-first CSS framework
- DaisyUI: Plugin for Tailwind CSS that provides UI components
- FastAPI: A modern, fast, web-based, Python framework for building APIs
- OpenAI GPT API: Generative AI API for generating goal suggestions
- MongoDB/PostgreSQL: Databases for storing goal data

---
## Solution

Professionals and students struggle with setting, tracking, and achieving their goals. They often use multiple platforms to manage their tasks, appointments, and goals, leading to disorganization and inefficiency. Existing solutions may not offer seamless integration with commonly used calendar applications like Google and Outlook, making it difficult for users to synchronize their goals and tasks with their schedules. Furthermore, these solutions may not use advanced AI Large Language Models (LLMs) to provide personalized goal recommendations and progress tracking.

---
## Installation


Clone the repository:

```sh
git clone git@github.com:xyzvora/achievaim
```

Navigate to the project directory:

```sh
cd achievaim
```

Install the dependencies:

```sh
npm install
```

Create a .env file in the root directory and provide the necessary environment variables:

```sh
API_KEY=<your-openai-api-key>
DB_URI=<your-database-connection-uri>
```

Usage
Start the development server:

```sh
npm run dev
```

Open your browser and visit http://localhost:5000 to access the app or relevant localhost address generated after running. 

```sh
npm run dev
```

Contributing
Contributions are welcome! If you find any issues or want to contribute to the project, please create a pull request or open an issue.

License
This project is licensed under the MIT License.

Feel free to modify and customize the README file according to your project's specifics.
