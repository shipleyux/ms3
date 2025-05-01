## ✅ HTML Validation

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




