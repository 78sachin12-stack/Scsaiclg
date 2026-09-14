# SCS AIC School Website & Portal — Vercel-ready

Official website and secure school portal for **Shree Chhattar Singh Arya Inter College, Khanpur • Bajna • Mathura**.

## Vercel deployment
Deploy the **project root** (the folder containing `index.html` and `vercel.json`).

- `/` → public school Home page
- `/portal.html` → Student / Staff login portal
- `/api/` → optional FastAPI API function

Do **not** set the Vercel Root Directory to `backend` or `frontend` for this package.

## Included
- Public Home page: school information, notices, upcoming events, gallery, admissions/enquiry, contact and portal access
- Admin / Clerk workspace
- Teacher portal
- Student portal
- Supabase Auth + RLS integration
- Website settings
- Students, teachers, attendance, results, fees, admissions, enquiries and notices
- Only the Supabase publishable key is used in browser code

## Local frontend
Open `index.html` for the public website or `portal.html` for the portal.

## Supabase
The browser uses the project's publishable key only. Never put a Supabase service-role key in frontend files.
