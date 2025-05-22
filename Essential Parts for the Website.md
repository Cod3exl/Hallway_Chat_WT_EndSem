# Essential Parts for the Website

## 1. Header

**Where:** `base.html`

**How:** Contains the logo (clickable to home), navigation links, and user profile info.

---

## 2. Form

**Where:** `auth/login.html`, `auth/register.html`, `chat/chat.html` (add contact, send message)

**How:** All user input (login, register, add contact, send message) uses forms with CSRF protection.

---

## 3. CTA Button

**Where:** `home.html`, `chat/chat.html`

**How:** Prominent buttons for Login, Register, Add Contact, Accept/Decline Invite, and Send Message.

---

## 4. Links

**Where:** Navigation in `base.html`, links in `home.html`, contact links in `chat/chat.html`

**How:** All navigation and actions are accessible via clear, styled links.

---

## 5. Hero Section

**Where:** `home.html`

**How:** The main landing section with a welcoming message and call-to-action buttons.

---

## 6. Footer

**Where:** `base.html`

**How:** Contains copyright, privacy policy, and terms.

---

## 7. Product Images

**Where:** User avatars (`Profile.avatar`), default icons in `chat/chat.html`

**How:** Users can upload avatars; default icons are shown if none is set.

---

## 8. Slider

**Where:** Not implemented (not typical for chat apps), but could be added for featured users or announcements.

---

## 9. Menu and Navigation

**Where:** `base.html` (desktop and mobile nav), `material.js` (mobile menu)

**How:** Responsive navigation bar and mobile drawer for easy access to all parts of the app.

---

## 10. Cards and Favicon

**Where:** Message bubbles in `chat/chat.html` (styled as cards), favicon in `static/images/favicon.ico`

**How:** Each message is a card; favicon is set for browser tabs.

---

## Summary Table

| Guideline/Part              | Where/How in Project                  |
| --------------------------- | ------------------------------------- |
| User-Centered Design        | All templates, user flows             |
| Responsive Web Design       | styles.css, material.css              |
| Performance Optimization    | Static files, AJAX polling            |
| SEO                         | Meta tags in base.html                |
| Content Strategy            | Clear text in all templates           |
| Cross-Browser Compatibility | HTML5/CSS3/JS standards               |
| Accessibility               | Semantic HTML, labels, color contrast |
| Mobile-First Development    | CSS media queries                     |
| Project Management          | Structure, README.md                  |
| Testing/QA                  | tests.py, Django admin                |
| Header                      | base.html                             |
| Form                        | login.html, register.html, chat.html  |
| CTA Button                  | home.html, chat.html                  |
| Links                       | Navigation, contacts, actions         |
| Hero Section                | home.html                             |
| Footer                      | base.html                             |
| Product Images              | User avatars, icons                   |
| Slider                      | (Not present, but can be added)       |
| Menu and Navigation         | base.html, material.js                |
| Cards and Favicon           | Message bubbles, favicon.ico          |

</rewritten_file>

