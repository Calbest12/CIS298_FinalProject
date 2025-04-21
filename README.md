# CIS298_FinalProject
First Commit (Calli) - Started with creating the admin login page
                     - Username: callibest
                     - Password: Maverick$12
                     - Then created main page to show recipes and be able to add them. 

Second Commit (Zach) - Wanted to implement the Spoonacular API so added the API key to settings.py
                     - Created my own login credentials of:
                     - username: zachw
                     - password: Recipe$123  
                     - Created a services.py file to handle all the API interactions
                     - updated forms.py, views.py, urls.py
                     - added base.html (updated existing html files with this integration)
                     - added search_results.html and recipe_detail_api.html for ability to utilize API on the user's end

Third Commit (Khalil) - Enhanced the website's base design and interactivity:
                      - Modified the base.html file to improve the navigation bar's appearance and user experience.
                      - Navbar Hover Effect: Added hover effects on the navigation bar links, including a background color                              change to white and text color change to lighter blue (#007bb5) when the user hovers over them.
                      - Highlight and Border-Radius Effect: Added a subtle border-radius and highlight effect when hovering on                          the navbar links to make the navigation smoother and   more visually appealing.
                      - Updated Color Scheme: Refined the color scheme, incorporating a light cyan background and complementary                         shades of blue for a modern, cohesive look.
                      - Improved Layout: Adjusted the layout for a cleaner, more user-friendly design.

Fourth Commit (Calli) - Created ability for users to log in and logout (returns to home page)
                      - Created a home page showing most viewed and highest rated recipes (Ability to rate recipes needs to be                          implemented)
                      - Users can view all recipes they've added when logged in
                      - Ability to add images to recipes
                      - Need to edit home page to show who submitted what reciepes and have added images show up when you view                          a recipe created by a user

Fifth Commit (Calli) - Fixed image issues where image was not showing up upon viewing recipe or having image saving correctly                          from when recipe was adding

Sixth Commit (Zach)   - Added the ability for user's to delete recipes from their saved recipe lists
                      - Added recipe_delete function to views.py, URL route added to urls.py, and a new recipe_delete.html for                          proper user interaction
                      - Also updated recipe_detail_local.html and recipe_my_list.html to include delete buttons

Seventh Commit (Zach) - Added the ability to edit recipes after they are initially saved. Allowing for accessibility options if                         the user has a mistype.
                      - Added recipe_edit function to views.py, URL route added to urls.py, and a new recipe_edit.html for                              accessbility
                      -  Also updated recipe_detail_local.html and recipe_my_list.html to include edit buttons

Eighth Commit (Khalil) – Added working recipe rating system (1-5 stars)
                       - Set up a new Rating model in models.py to let users rate each recipe from 1 to 5. Each user can rate a recipe.
                       - Created a new RatingForm in forms.py to make submitting ratings easy through a dropdown.
                       - Updated the views.py file, specifically in the recipe_detail_local view, to show the rating form on each recipe page and process it when submitted. After a user rates a recipe, it updates the recipe's average rating automatically using a custom method called update_rating().
                         -Edited the recipe_detail_local.html template to display the rating form right below the recipe details so users can submit their score.
                         - After you add a recipe, you can go to its detail page and scroll down to the rating section. From there, you can pick a number from 1 to 5 and submit your rating. A success message will show up confirming your rating was saved.
                          - Also double-checked urls.py to make sure the path for viewing individual recipes (/recipe/<int:pk>/) is correctly pointing to the updated detail view that handles ratings.
                         -Ran database migrations to create the new recipes_rating table. If you get an error like "no such table: recipes_rating", it means you forgot to run the migrations after adding the model.

Ninth Commit (Calli) - Give users the ability to write comments on user generated receipes. This allows Users to be able to give their reviews about specific recipes and for otheer users to be able to see who wrote what, and what they have to say. 
                      - Set up a commenting model and form in models.py and forms.py respectively. Updating views.py and the recipe_detail_local.html template to allow users to write their comments and have them saved and submitted correctly.

Tenth Commit (Calli) - Populated the Recipes to have fields for presentation for class and ability to show off different areas of the website. Also clean up the code for final submission. 

Calli Best Group Eval - [GroupEval.docx](https://github.com/user-attachments/files/19828601/GroupEval.docx)
Khalil Aun Group Eval - [Khalil Group Eval.docx](https://github.com/user-attachments/files/19838502/Khalil.Group.Eval.docx)
