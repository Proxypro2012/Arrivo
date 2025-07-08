# 🚌 Arrivo

**Arrivo** is a sleek, modern, and real-time **school bus tracking app** built using **SwiftUI** and **Firebase**. Designed for both students and school admins, it provides a beautiful glassmorphism-inspired interface and intuitive controls to track bus arrival statuses like `Coming`, `Arrived`, and `Left`.

> 📱 Made for iPadOS and macOS (SwiftUI)  
> ☁️ Powered by Firebase Realtime Database and Firebase Authentication  
> 🌈 Designed with animation, fluid transitions, and a minimalist aesthetic

---

## ✨ Features

### 🎒 For Students
- View a live-updating **list of buses**
- See each bus's status in **real time**
- Beautiful **capsule-style indicators** with color-coded statuses:
  - 🟢 Arrived
  - 🟡 Coming
  - 🔴 Left

### 🛠️ For Admins (and/or Teachers)
- Log in securely via **Firebase Auth**
- Set status for each bus using a **3-way toggle switch**
- Automatically resets buses to `Coming` at **midnight**
- All changes sync **instantly** with Firebase for students to see

### 🎨 Visual Design
- **Glassmorphism**: sleek blurred cards and layered gradients
- **Smooth transitions**: animated views, fading background layers
- **Spring-based motion effects** for clean, modern UI

---

## 📸 Screenshots

| Role Selector | Student View | Admin Dashboard |
|---------------|--------------|-----------------|
| ![role](docs/role.png) | ![student](docs/student.png) | ![admin](docs/admin.png) |

> *(Add your own screenshots in a `docs/` folder!)*

---

## 🔧 Technologies Used

- **SwiftUI** – UI framework with animations and transitions
- **Firebase Authentication** – email-based login & signup
- **Firebase Realtime Database** – instant bus status sync
- **Combine** – reactive state management
- **Glassmorphism** – for iOS-style elegant design

---

## 📦 Project Structure

Arrivo/
├── AppState.swift # Global app state, Firebase listeners
├── ContentView.swift # View routing + background transitions
├── AdminDashboardView.swift # Admin tools with 3-way status toggles
├── StudentDashboardView.swift # Live bus display for students
├── Bus.swift # Bus model
├── FirebaseService.swift # Auth + DB write operations
├── Assets, Info.plist # App assets and Firebase config


---

## 🔐 Authentication

Admins are required to:
- Sign up with a **verified email**
- Confirm via **email verification**
- Login using **Firebase Authentication**

No student login is required.
