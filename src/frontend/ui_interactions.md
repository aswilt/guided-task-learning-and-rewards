# Frontend UI Interactions

This document outlines the conceptual user interactions and flows for the Guided Task Learning and Rewards system from a TPM perspective. All frontend behavior is **agnostic but designed to sit atop enterprise platforms like Oracle**.

---

## Overview

- The system is accessed as a **pop-up window** within the enterprise platform.  
- Users can view **leaderboards, challenge period metrics, and configurable parameters**.  
- Points are accrued through actions completed in the underlying enterprise platform (“Oracle”) workflows.  
- The frontend is designed to be **modular and decoupled**, allowing integration with multiple backend or workflow systems.

---

## UI States and Interactions

1. **Dashboard / Pop-up Window**  
   - Displays current point totals, active challenges, and leaderboard rankings  
   - Allows users to see their progress relative to peers  

2. **Task Guidance Flow**  
   - Each workflow step is presented sequentially within the pop-up  
   - Guidance text explains what action to complete in the enterprise system  
   - Rewards and points are shown in real-time as steps are completed  

3. **Reward and Leaderboard Updates**  
   - Challenge period metrics update dynamically based on completed actions  
   - Points accrue automatically when tasks in the enterprise platform are detected as completed  
   - Administrators can configure challenges, rewards, and deadlines from the backend  

4. **Edge / Blocked States**  
   - If prerequisites for a task are not met, the UI displays a “blocked” state with instructions  
   - Users are guided to complete missing steps before advancing  

---

## TPM Perspective

- Demonstrates understanding of **user experience design** without needing full production frontend code  
- Shows how **gamification, guided learning, and backend interactions** are surfaced to users  
- Provides a blueprint for engineering teams to implement the pop-up UI and integration points  
- Emphasizes **flexibility and modularity**, allowing adaptation to different enterprise systems
