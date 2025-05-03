## Code Validation

All HTML files were tested using the [W3C Markup Validator](https://validator.w3.org/). Template-specific Django tags (`{% %}`, `{{ }}`) were ignored during validation, and all structural HTML errors were corrected.

<details>
<summary><strong>✔ base.html</strong> – Passed with minor template tag warnings</summary>

**Notes:**
- Fixed missing `lang="en"` attribute.
- Ensured `<title>` is correctly placed within `<head>`.
- Stray template tags caused warnings but were not actual HTML issues.

**Status:** ✅ Pass

<img width="1170" alt="base.html validation" src="https://github.com/user-attachments/assets/0c81dd94-162b-4c8e-b55e-a0a832b2d805" />
</details>

<details>
<summary><strong>✔ post_form.html</strong> – Passed</summary>

**Notes:**
- No structural errors.
- All tags properly closed and nested.

**Status:** ✅ Pass

<img width="1217" alt="post_form.html validation" src="https://github.com/user-attachments/assets/d525a3c8-05ab-4d38-9edb-d4da8ce53379" />
</details>

<details>
<summary><strong>✔ post_detail.html</strong> – Passed</summary>

**Notes:**
- All content properly structured.
- Page passed validation cleanly.

**Status:** ✅ Pass

<img width="1225" alt="post_detail.html validation" src="https://github.com/user-attachments/assets/d97924dc-b543-47db-b55b-5546eb805d6b" />
</details>

<details>
<summary><strong>✔ post_list.html</strong> – Passed</summary>

**Notes:**

### 🟡 Warning: Empty `<h5>` Heading Elements
- **No fix required.** These were false positives caused by empty template tags like `{{ comment.author }}` when no value was rendered.
- Example:
  ```html
  <h5 class="card-title">{{ comment.author }}</h5>
  ```

### 🔴 Error: `<p>` Inside `<h5>`
> **Error:** Element `<p>` not allowed as a child of element `<h5>` in this context.

#### Cause:
A `<p>` tag (block-level element) was nested inside a heading element, which violates HTML rules — only phrasing content is allowed inside headings.

#### Fix Implemented:
Updated this:

```html
<h5>
  Comment title
  <p class="text-muted small mb-1">Posted on 1 May 2025</p>
</h5>
```

To:

```html
<h5>Comment title</h5>
<p class="text-muted small mb-1">Posted on 1 May 2025</p>
```

**Status:** ✅ Pass

<img alt="post_list.html validation" src="images/testing/post-form-html-validation.png" />

</details>

<details>
<summary><strong>✔ post_confirm_delete.html</strong> – Passed</summary>

**Notes:**
- Form markup validated successfully.
- Required fields are correctly labelled and accessible.

**Status:** ✅ Pass

<img width="1417" alt="post_confirm_delete.html validation" src="https://github.com/user-attachments/assets/0cddce43-b6d6-4df2-ba70-ff54936dc100" />

</details>

<details>
<summary><strong>✔ delete_comment.html</strong> – Passed</summary>

**Notes:**
- Minimal page with no structural issues.
- Confirmed basic form and button layout were valid.

**Status:** ✅ Pass

<img width="1196" alt="delete_comment.html validation" src="https://github.com/user-attachments/assets/b7cdefd6-1b57-4c64-a4a2-56c0632cd9d0" />

</details>


<details>
<summary><strong>✔ logout.html</strong> – Passed</summary>

**Notes:**
- Minimal page with no structural issues.
- Confirmed basic form and button layout were valid.

**Status:** ✅ Pass

<img width="1226" alt="Image" src="https://github.com/user-attachments/assets/33384891-59f6-47cf-8865-2c80e61862d9" />

</details>


<details>
<summary><strong>✔ edit_comment.html</strong> – Passed</summary>

**Notes:**
- Minimal page with no structural issues.
- Confirmed basic form and button layout were valid.

**Status:** ✅ Pass

<img width="1239" alt="Image" src="https://github.com/user-attachments/assets/9a3564b3-e23a-438c-835b-6a94b4d12458" />

</details>

<details>
<summary><strong>✔ signup.html</strong> – Passed</summary>

**Notes:**
- Minimal page with no structural issues.
- Confirmed basic form and button layout were valid.

**Status:** ✅ Pass

<img width="1224" alt="Image" src="https://github.com/user-attachments/assets/e5f44b26-4959-412e-b368-3b4d97cfa268" />

</details>

<details>
<summary><strong>✔ login.html</strong> – Passed</summary>

**Notes:**
- Minimal page with no structural issues.
- Confirmed basic form and button layout were valid.

**Status:** ✅ Pass

<img width="1112" alt="Image" src="https://github.com/user-attachments/assets/7e75a2bf-3a3d-40a7-921b-ceafb7681031" />

</details>

<details>
<summary><strong>✔ logout_success.html</strong> – Passed</summary>

**Notes:**
- Minimal page with no structural issues.

**Status:** ✅ Pass



</details>

---
<details>
<summary><strong> CSS Validation</strong> – Passed</summary>

All custom CSS was tested using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to ensure compliance with modern web standards.

The main stylesheet (`style.css`) was uploaded directly to the validator. The results showed no syntax errors or compatibility warnings.


**Status:** ✅ Pass

<img src="docs/images/css.png" alt="CSS">

</details>

---

### PEP 8 Compliance

All Python files were checked for PEP 8 compliance using the [PEP8 CI tool](https://pep8ci.herokuapp.com/).  
Warnings and errors were resolved where appropriate to ensure code quality and readability.

---
## Accessibility 

This site was tested using the WAVE Web Accessibility Evaluation Tool to help ensure it is usable by as many people as possible, including those using screen readers or keyboard navigation.

All critical issues were resolved, including:

- Making sure every image has alt text
- Ensuring that every page has a proper heading structure (with one main heading)
- Removing empty heading tags that were confusing for screen readers
- Adding descriptive link text (like “Read more about this post”) where needed
- Including a hidden heading in the site’s layout to support screen readers
- **Redundant Links**: WAVE flagged multiple links pointing to the same destination within each blog card — for example, both the post title and a "Read more" button linking to the full post. While this is a common and user-friendly design pattern, it was reviewed for accessibility. To reduce potential confusion for screen reader users, one of the duplicate links was removed, leaving a single clear and descriptive link per card.
- **Low Contrast Buttons**: WAVE identified that the original "Edit" and "Delete" comment buttons had low contrast due to Bootstrap's `outline` button styles. These were updated to solid `btn-secondary` and `btn-danger` styles with white text to ensure they are readable and accessible to all users.

Some common blog patterns, like linking both the post title and a “Read more” button to the same page, were kept for usability but reviewed to make sure they didn’t cause confusion.

The site now passes accessibility checks and offers a user-friendly experience across devices and assistive technologies.


<details>
<summary><strong>View WAVE Accessibility Homepage Screenshots</strong></summary>

<img src="docs/images/wave1.png" alt="Wave Test Homepage">

</details>

<details>
<summary><strong>View WAVE Accessibility Post Detail Page Screenshots</strong></summary>

<img src="docs/images/wave2.png" alt="Wave Test Homepage">

</details>

<details>
<summary><strong>View WAVE Accessibility Create Post Page Screenshots</strong></summary>

<img src="docs/images/wave3.png" alt="Wave Test Homepage">

</details>

<details>
<summary><strong>View WAVE Accessibility Sign Out Page Screenshots</strong></summary>

<img src="docs/images/wave5.png" alt="Wave Test Homepage">

</details>

<details>
<summary><strong>View WAVE Accessibility Login Page Screenshots</strong></summary>

<img src="docs/images/wave4.png" alt="Wave Test Homepage">

</details>

<details>
<summary><strong>View WAVE Accessibility 404 Page Screenshots</strong></summary>

<img src="docs/images/wave6.png" alt="Wave Test Homepage">

</details>

---

## Lighthouse Audit Results (Chrome DevTools)



<details>
<summary><strong>View Lighthouse Test Screenshots</strong></summary>

_Add screenshots here showing Lighthouse scores and reports for homepage and post pages._

</details>


Lighthouse was run on the live site using Chrome DevTools to assess accessibility, performance, SEO, and best practices. Results were consistent across multiple key pages.

| Metric        | Score Range (Out of 100) | Notes                                                         |
|---------------|--------------------------|---------------------------------------------------------------|
| Accessibility | 95–100                   | Strong use of alt text, labels, proper landmarks, and heading order. |
| Performance   | 90–100                   | Optimized images, lazy loading, and minimal unused JS/CSS.    |
| SEO           | 100                      | All pages include meta titles, descriptions, and semantic HTML. |
| Best Practices| 100                      | Site uses HTTPS, avoids deprecated APIs, and passes audits.   |
---
###  Performance Optimization: Removal of Post Images

To improve Lighthouse performance scores and ensure a faster, more accessible user experience, post images were removed from the blog listing page (`post_list.html`).

#### Reason for Removal

During testing, including images on every post caused several issues:

-  Lower Lighthouse Performance Scores (sometimes as low as 65)
-  Slower Largest Contentful Paint (LCP)
-  Increased total network payload
-  Higher Cumulative Layout Shift (CLS)
- Layout inconsistencies on mobile devices

Even with lazy loading and Cloudinary optimizations, these image-heavy layouts significantly impacted performance.

#### Result After Removal

- ✅ Lighthouse score improved to 96+ for Performance
- ✅ CLS dropped close to 0
- ✅ Page load time visibly improved on slow connections
- ✅ Better consistency and layout stability across screen sizes

Removing images was a tradeoff for performance and user experience. A clean, minimal layout was prioritized for clarity and readability, especially on mobile devices.


---
