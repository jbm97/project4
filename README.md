# SEPBT220 Project 4: Personal Finance Tracker App

## Project Description
My Project 4 is a personal finance management application that allows users to track their income and expenses, categorize transactions, and visualize their financial data through charts and/or graphs and images. The goal is to provide users with insights into their spending habits and help them make better financial decisions.

## Project Links
- [Live Demo]()

## Technologies Used
- Backend: Django, Python, PostgreSQL
- Frontend: CSS, JavaScript, Django Templates

## Features
- Add, edit, and delete transactions
- Categorize transactions as income or expense
- View summary reports and charts
- Filter transactions by date and category

## ERD

### User
- username
- firstname
- lastname
- age (DOB)

### Transaction
- id
- title
- amount
- date
- type (Income/Expense)
- category_id
- user_id

### Category
- id
- name
- user_id 

## Account
- id
- name
- balance
- user_id

## Wireframe

Will hopefully make photos, but:
- Home Page: Overview of transactions and summary charts
- Add Transaction Page: Form to add a new transaction
- Edit Transaction Page: Form to edit an existing transaction
- Reports Page: Detailed reports and charts
- Accounts Page: More detailed page for personal accounts

## Routes

GET home page, /

GET, POST transactions/add, category/add, accounts/add
GET, POST transactions/:id/edit, category/:id/edit, accounts/:id/edit
GET, POST transactions/:id/delete, category/:id/delete, accounts/:id/delete

