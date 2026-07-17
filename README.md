# Alura Album - Tech World Cup

A virtual and interactive sticker album focused on the greatest names and technologies in the world. This project uses native web technologies to create a rich experience, including 3D page-flip effects and procedural sounds, while consuming data from an API.

## Project Objective

The main objective of "arquitWithIA" is to apply architectural rigor, *Clean Code*, and *Separation of Concerns (SoC)* in building a modern frontend application. The application simulates a physical sticker album in the browser, dynamically fetching data (sticker images) from a backend and injecting them into the appropriate slots in a performant and smooth way.

## File Structure

Currently, the project base is distributed across the following main files:

- **`index.html`**
  Responsible for the application's skeleton and the album's structure. It contains the navigation controls (arrows and sound button), the markup for the 3D album layout, and the pages organized by technology areas (AI, Python, Databases, Operating Systems, etc.).

- **`style.css`**
  Responsible for all the visual aspects and the premium feeling of the application. It uses a design based on CSS variables (design tokens) and encompasses everything from the layout structure (Flexbox/Grid) to complex animations (glitch effects on the cover, 3D rotations of elements, and dynamic shadows to simulate the page spine).

- **`app.js`**
  The current "engine" of the frontend. It centralizes the initialization of the external page-flip library (`page-flip`), the API consumption (`fetch` to `localhost:8000`) to inject the sticker images into the correct slots, the control of mouse/touch drag events, and the procedural sound synthesis using the *Web Audio API* to simulate paper friction.
