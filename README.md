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
