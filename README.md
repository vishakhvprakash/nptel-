# Replicated SWAYAM / NPTEL Course Progress Website

This project is a high-fidelity replica of the **SWAYAM - NPTEL Student Progress Report** page for the course **Deep Learning - IIT Ropar** (`noc26_cs138`), replicated directly from the provided MHT archive.

## Directory Structure
- `index.html`: Fully self-contained, interactive standalone web page.
- `assets/`: All local resources extracted and bundled:
  - `Swayam_logo.svg` & `dark_theme_swayam_logoNew.svg` (Swayam logos for light/dark themes)
  - `NPTEL-logo-new.png` (High-resolution NPTEL partner logo)
  - `accessibility_icon.svg` & `accessibility_dark.svg` (Accessibility action icons)
  - `106_hfdougdxv.css`, `3piepmm47cc3f.css`, `33dt0f8m0h8si.css`, `38-6-b6tu4i96.css` (Tailwind & Next.js styling)
  - `toastify.css`, `radix.css`, `roboto.css` (Component & font styles)
- `preview.png`: Visual screenshot of the rendered webpage.

## Included Features & Data
- **Student Profile & Course Summary**:
  - Name: **Jijohns Johnson**
  - Email: **jijohnsjohnson178@gmail.com**
  - Enrolled Date: **2026-08-02**
  - Course Progress: **93.33%** with circular SVG gauge
- **Interactive Accordions**:
  - **Unit Wise Progress**: Detailed lesson and assignment completion breakdown across Weeks 1–12 and supplementary units.
  - **Assignment Scores**: Expandable breakdown with assignment status, percentage bars, and scores.
  - **Grading and Certifications Policy**: Official NPTEL certification criteria (best 8 of 12 assignments + 75% proctored exam weightage).
- **Interactive UI Components**:
  - Accessibility tools modal (Font scale A-/Reset/A+, Light/Dark theme switcher, High contrast toggle)
  - User profile menu for Jijohns Johnson
  - AI Powered Widgets slide-out assistant panel
  - Responsive mobile and desktop layouts
