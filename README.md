# Aayush Tyagi — Personal Portfolio Website

🔗 **Live Link:** [https://aayushtyagi550.github.io/Portfolio/](https://aayushtyagi550.github.io/Portfolio/)

A premium, highly interactive personal portfolio website designed for **Aayush Tyagi**, a Software Engineer specializing in Java, Data Structures & Algorithms, and Full-Stack (MERN) Development. Built with clean semantic HTML, modular vanilla CSS, and performance-optimized vanilla JavaScript.

---

## 🛠️ Tech Stack & Technologies

* **Core Structure**: HTML5 (Semantic elements for maximum SEO friendliness and accessibility).
* **Styling System**: CSS3 (Vanilla design tokens, Custom HSL variables, Flexbox & Grid layouts, Glassmorphism).
* **Interactions & Logic**: Native Vanilla JavaScript (ES6+), optimized for hardware-accelerated animations.
* **Typography Pairing**: Google Fonts (`Playfair Display` for headings, `Plus Jakarta Sans` for body copy, `JetBrains Mono` for codebase technical labels).
* **Iconography**: Embedded SVG Path-based Lucide icons (reducing external HTTP requests to zero for instantaneous load times).

---

## ✨ Features & Highlights

### 🎨 Design System & Visual Aesthetics
* **Harmonious Color Palette**: Designed around a premium **Brown & Cream** palette. Features a soft off-white cream background (`#fbf9f5`), rich chocolate brown text/elements (`#2a1e17`), and warm sand/gold accents (`#b3855c`).
* **Adaptive Dark Mode**: Toggles smoothly with a custom transition animation class. In dark mode, the page adapts to a rich obsidian dark chocolate base (`#120b08`), maintaining legibility with custom glossy gradients, high-contrast text, and a glowing golden button focus.
* **Glassmorphic Navigation Bar**: An interactive floating header with deep blur properties (`45px` blur), saturation boosters (`220%`), and polished edge bevel reflections. Responsive styling adapts from a frosted-glass pill header in light mode to a deep obsidian bar in dark mode.
* **Ambient Floating Orbs (Option A)**: Features three large, highly blurred glowing background orbs (Gold, Amber, and Bronze) that float at different scroll depths, rotating and scaling dynamically.
* **Tech Dot Grid**: A repeating geometric dot matrix pattern styled on the body that shifts color dynamically between theme states (light brown in light theme, gold in dark theme).

### 🕹️ Interactive Features
* **Magnetic Snapping Cursor**: A custom dual-element cursor (inner dot + trailing outer halo).
  - *Standard Mode*: Follows the mouse with physics-based lag.
  - *Magnetic Snap*: Snaps onto small interactive targets (links, icons, buttons) and morphs its width, height, and border-radius to wrap around them perfectly.
  - *Expansion Mode*: Expands to a large circular hover ring when hovering over larger interactive components (cards, mockups).
  - *Click state*: Shrinks the halo and shifts color to warm orange-gold on click.
* **Buttery-Smooth 3D Card Tilt**: Certification cards feature dynamic mouse-follow 3D tilt effects.
  - *Hit-Testing Stability*: Optimized using `pointer-events: none` on the card layer to prevent browser 3D projection hit-testing thrashing (no jittering/flickering).
  - *Performance Caching*: Caches bounding client dimensions on mouse enter to avoid layout thrashing in the mousemove handler.
* **Project Mockup Sliders**: Projects (SymptoGenie and MelodyVerse) are showcased in clean web browser mockups with autoplaying and manually clickable screenshot sliders.
* **Staggered Animations**: Dynamic drop-in transitions, typewriter effects for lists, skill capsule slide-ups, achievements count-ups, and trophy badge pops triggered using a high-performance scroll-spy Intersection Observer.
* **Dynamic Card Console Logging**: Hovering over individual skill capsules dynamically streams a custom real-time diagnostic verification message to the terminal logger box (`.card-console-log`) at the bottom of that category card.

### ⌨️ Terminal Vibe & Interactive CLI widget
* **Interactive Terminal CLI Widget**: A persistent retro-futuristic terminal coin button floats in the bottom-right. Clicking it slides up a custom dark chocolate terminal overlay (`#120b08`) with a gold border.
  - *Commands*: Supports typing commands with instant output feeds and scroll-to-bottom mechanics:
    - `help` / `h`: Lists all available commands.
    - `about` / `a`: Outputs a bio of Aayush.
    - `skills` / `s`: Prints system categories and loaded modules configuration status.
    - `projects` / `p`: Lists SymptoGenie and MelodyVerse with clickable hyperlinks.
    - `education` / `e`: Prints academic qualifications and timeline (B.Tech, Class 12th, Class 10th).
    - `contact` / `c`: Displays email, GitHub, LinkedIn, and LeetCode links.
    - `exit` / `t`: Closes the terminal panel overlay.
    - `clear`: Clears log history.
  - *Auto-quote stripping*: Intelligently handles inputs wrapped in quotes (e.g. typing `'c'` or `"c"`).
* **Monospace Typography Toggler ("Terminal Font Mode")**: Adds a `>_ MONO` toggle button in the navbar right group. Swaps the entire page's typography dynamically to monospace (`JetBrains Mono`), transforming it into a clean typewriter layout. Saves choice in `localStorage`.
* **Startup Boot Sequence Overlay**: Displays a simulated system boot sequence (`#bootOverlay`) showing core modules mounting. Runs for 1.8s (or until Esc / Skip Button is clicked) on first load. Tracked in `sessionStorage` to run only once per browser session.
* **Global Keyboard Navigation Hotkeys**: Pressing keyboard hotkeys (when console is closed) scrolls the page:
  - `` ` `` / `t`: Toggle CLI console.
  - `s`: Skills section.
  - `p`: Projects section.
  - `c`: Contact section.
  - `e`: Education section.
  - `a`: About section.
  - *Note: Intelligently disabled when typing inside form inputs.*


---

## 📂 Project Structure & Section Walkthrough

### 1. Header (Navbar)
* Contains the brand logo with a terminal prompt layout `aayush.tyagi_` featuring a gold dot and an animated blinking cursor.
* Links to the downloadable resume PDF (`assets/Aayush_Tyagi_Resume.pdf`).
* Includes the Dark Mode toggle that updates theme variables and transitions colors smoothly.

### 2. Landing (Hero)
* Expressive text layout displaying credentials and a brief tagline.
* Staggered animation cards sliding up into place on initial page load.

### 3. About Me
* A 2-column layout displaying the avatar image, work call-to-actions, and professional summary.
* Features two interactive 3D Y-axis flipping cards detailing **Mission** and **Vision** values.

### 4. Education
* Vertical timeline showing scholastic milestones (B.Tech, Class 12th, Class 10th).
* Bullet points animate in sequentially with typewriter spacing, cap icons toss on hover, and an SVG border trace draws itself when hovered.

### 5. Projects
* Showcases two full-stack web applications:
  - **SymptoGenie**: AI-integrated symptom analyzer and report generator.
  - **MelodyVerse**: Full-stack music community platform.
* Project screenshots cycle automatically every 3.5 seconds inside high-fidelity browser mockup frames.

### 6. Skills
* Skill categories (Languages, Frontend, Backend, Databases, Core CS, Tools) arranged in a 3-column grid.
* Contains fully rounded, capsule-shaped skill badges featuring official brand-colored SVG icons, monospace font names, and a pulsing status dot showing running modules.
* Features a terminal box (`.card-console-log`) at the bottom of each card that dynamically streams custom diagnostic logs in real-time when hovering over badges.
* Svg header category icons spin `360deg` on hover.

### 7. Certifications
* Contains HackerRank and UiPath developer credentials.
* Powered by the optimized 3D tilt script to provide depth and interactive tracking.

### 8. Achievements
* Displays LeetCode (300+ solved) and Production Apps metrics using live count-up stats counters, coupled with popup trophy badges.

### 9. Contact
* *Left Column*: Clean contact form featuring active floating inputs and golden glowing underline drawing states.
* *Right Column*: Fixed-color dark chocolate information sheet (`#2a1e17` card) with light text (`#fbf9f5`) and sand labels (`#cbbcb3`), ensuring high legibility in both light and dark themes.

---

## 🚀 Local Development

Since the portfolio is built on native web standards, you can run it locally without compiling.

### 1. Clone the repository
```bash
git clone https://github.com/Aayushtyagi550/Portfolio.git
cd Portfolio
```

### 2. Run a local server
To ensure that all assets, custom cursors, and JavaScript events load properly with correct MIME types, run a simple local web server:

**Using Node.js (`npx`):**
```bash
npx serve .
```

**Using Python:**
```bash
python -m http.server 3000
```

Open `http://localhost:3000` (or the port specified by the server) in your browser.

*Note: If you modify the CSS or JavaScript files, perform a hard refresh (**`Ctrl` + `F5`** or **`Ctrl` + `Shift` + `R`**) to bypass browser cache.*

---

## 🌐 Deployment

This website is statically self-contained and is ready for production deployment:

### GitHub Pages (Recommended)
1. Go to your repository settings on GitHub.
2. Navigate to **Pages** in the left sidebar.
3. Under **Build and deployment**, set the source to **Deploy from a branch**.
4. Choose `main` and select the `/ (root)` folder, then click **Save**.

### Vercel / Netlify
Simply import the repository. Since it has no build step, Vercel/Netlify will automatically detect it as a static website and host it instantly.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
