## Debugging Report - Sober Spaces Django Blog


## Table of Contents 

- [Part 1 - Debugging the Author Field and Missing Edit/Delete Buttons](#part-1---debugging-the-author-field-and-missing-editdelete-buttons)
- [Part 2 - Debugging the Signup and Login Flow](#part-2---debugging-the-signup-and-login-flow)
- [Part 3 - Debugging Authorship, Permissions, and UI Feedback](#part-3---debugging-authorship-permissions-and-ui-feedback)
- [Part 4 - Bug Fixes Related to Categories and Templates](#part-4---bug-fixes-related-to-categories-and-templates)
- [Part 5 - Bug Fixes: Image Upload and Display-Pre removal](#part-5---bug-fixes-image-upload-and-display-pre-removal)
- [Part 6 - Comment Bugs and UI Issues](#part-6---comment-bugs-and-ui-issues)
- [Part 7 - Bug Fix: Active Category Button Not Highlighting](#part-7---bug-fix-active-category-button-not-highlighting)

---


### Part 1 - Debugging the Author Field and Missing Edit/Delete Buttons

During development, one issue I encountered was that the "Edit" and "Delete" buttons for blog posts were not appearing, even when I was logged in. After some investigation, I discovered that the problem was due to posts being created without an author value. Because the templates use a condition to check if the logged-in user is the post's author (`{% if user == post.author %}`), this condition always returned false. As a result, the buttons never rendered.

Later in development, I added an `author` field to the `Post` model using a `ForeignKey` to Django's `User` model. However, this led to a migration error:

`OperationalError: no such column: blog_post.author_id`

This happened because the existing posts in the database did not have any author field populated, so Django couldn't apply the migration without a default value.

To fix this, I updated the `Post` model to include the author field:

`author = models.ForeignKey(User, on_delete=models.CASCADE)`

Next, I updated the `post_create` view so that when a post is submitted, the current user is automatically assigned as the author. I used `form.save(commit=False)` to set the author before saving the post.

When I ran `python manage.py makemigrations`, Django asked how to populate the existing rows. I chose the option to "Provide a one-off default" and entered the ID of my superuser (which was 1). I then ran `python manage.py migrate`, which successfully updated the database.

To confirm the fix worked, I created a new post while logged in and verified that the author was now correctly set. The template condition `{% if user == post.author %}` now evaluated to true, and the edit/delete buttons appeared as expected.

* * * * *

### Part 2 - Debugging the Signup and Login Flow

I encountered several issues while integrating user authentication using Django Allauth.

**Redirect Loop**

Initially, when I visited the login or signup pages, they redirected straight back to the homepage without displaying the form. This turned out to be due to already being logged in. Allauth automatically redirects logged-in users. Visiting `/accounts/logout/` manually solved this and confirmed that the views worked once logged out.

**Signup Form Refreshing with No Feedback**

At one point, submitting the signup form caused the page to refresh silently, without showing any errors. To fix this, I added `{{ form.non_field_errors }}` to the template, which revealed any general form validation errors (e.g. weak passwords or mismatched fields).

I also included a hidden input to control redirect behavior after successful signup:

```html
<input type="hidden" name="next" value="/" />
```

**Email Verification Error**

Another issue occurred when Allauth tried to send a verification email. Since I had no mail server set up, this resulted in a `ConnectionRefusedError`. I fixed this by disabling email verification in `settings.py` for development:

<pre><code>ACCOUNT_EMAIL_VERIFICATION = "none" ACCOUNT_EMAIL_REQUIRED = False ACCOUNT_SIGNUP_FIELDS = ["username", "password1", "password2"] ACCOUNT_LOGIN_METHODS = {"username"} </code></pre>

In the custom signup form, I also removed the email field completely.


* * * * *

### Part 3 - Debugging Authorship, Permissions, and UI Feedback

**Field Conflict: `user` vs `author`**

In early versions of the app, I mistakenly added both a `user` and an `author` field to the `Post` model. This caused a `UNIQUE constraint failed` error when running migrations. I fixed this by removing the `user` field and retaining only `author = models.ForeignKey(User, ...)`, adding `related_name='posts'` for clarity and avoiding reverse lookup conflicts.

**Debugging UI Logic**

To verify if a logged-in user was correctly being recognised as the post's author, I added debug lines to the `post_detail.html` template:

```html
<p>Logged in as: {{ user }}</p>
<p>Post author: {{ post.author }}</p>
<p>Does user = author? {% if user == post.author %}TRUE{% else %}FALSE{% endif %}</p>

```

This confirmed that my condition worked and edit/delete buttons were properly restricted.

**Manual Testing**

I manually tested:

-   Creating, editing, deleting posts

-   User-specific visibility of action buttons

-   Permissions between different logged-in users

* * * * *

### Part 4 - Bug Fixes Related to Categories and Templates

**Problem: Categories Not Displaying**

After creating the `Category` model and assigning categories in the admin panel, I found that the homepage wasn't showing the category nav or post category names.

**Diagnosis**

This happened because I had two versions of the `post_list` view in `views.py`. The second one didn't include the required context (`categories`, `active_category`) and was overwriting the first.

**Fix**

I deleted the duplicate function and updated the correct one to pass all necessary context data.

**Result**

-   Categories appear above the post list

-   Posts display their assigned category

-   Filtering by category now works

* * * * *

### Part 5 - Bug Fixes: Image Upload and Display-Pre removal

**Please note: this feature was removed from the app**

**Issue 1: Image Field Missing**

I added an `ImageField` to the model, but it didn't appear in the form. This was due to a duplicate `PostForm` class in `forms.py`, and the one being used didn't include the `image` field.

**Fix**

I removed the duplicate and ensured the `image` field was included. I also added `enctype="multipart/form-data"` to the HTML form.

**Issue 2: IntegrityError on Edit**

Editing a post raised an `IntegrityError` due to missing `author_id`. The `post_edit` view was saving without re-setting the author.

**Fix**

I added `form.save(commit=False)` and reassigned the author before saving.

**Issue 3: Featured Image Showing on All Posts**

The loop was using `{{ featured_post.image.url }}` by mistake.

**Fix**

Replaced it with `{{ post.image.url }}` inside the loop and added separate CSS for featured and regular posts.

* * * * *

### Part 6 - Comment Bugs and UI Issues

**Buttons Not Showing**

The logic to show the edit/delete comment buttons was placed outside the comment loop. Moved it inside `{% for comment in comments %}` to evaluate correctly.

**Comment Field Not Clearing**

After submitting a comment, the form retained the text. I applied the `POST/Redirect/GET` pattern in the view so that after saving a comment, the user is redirected. This cleared the form and prevented duplicates.

* * * * *

### Part 7 - Bug Fix: Active Category Button Not Highlighting

When filtering posts, the "All" button stayed active and the selected category didn't appear highlighted.

**Diagnosis**

The `active_category` variable was not being passed correctly in the view.

**Fix**

I passed `active_category = category` from the view and used `.pk` for reliable comparison in the template.

**Result**

Now the correct category button highlights when selected, improving the user experience.

