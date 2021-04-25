# 🔍 Medicare-Plan-Search-Tool
Simple website that allows users to search Medicare plans

## Getting Started
You're free to use whatever libraries, packages, of frameworks you like. We're less interested in which technologies you're familiar with and more with how you utilize them. Here are some popular ones:
Meteor.js with React
Next.js
Create React App

Once you've made your tech selection, your web app should have the following capabilities:
  * Take as input a Bid ID
  * Search the provided list of Medicare Advantage plans for the relevant entry
  * Display the following information:
    * Insurance carrier
    * Plan name
    * Geographic area served by this plan
    * The link to the plan's pharmacy website

## Important Terms
Bid ID: A unique identifier for Medicare Advantage plans. Of the following two forms:
Hxxxx-xxx-xxx, where all digits are required (e.g. "H1234-007-003")
Hxxxx_xxx_y, where the final "y" group has no trailing zeroes (e.g. "H1234_007_3")

## Included Files
data/medicare_plans.txt - Contains basic information about Medicare plans. You'll use this file to search for Medicare Advantage plans.

## Running the Program
Node and npm should be installed for running the program.

Inside the directory, run the following:
`<npm install>`

Then, run the following to open the web app on your local browser:
`<npm run start>` 

