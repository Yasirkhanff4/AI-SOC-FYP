* {
  box-sizing: border-box;
}

:root {
  --bg: #07131d;
  --panel: #0d1c2b;
  --panel-strong: #10283a;
  --muted: #8aa0b6;
  --text: #ebf4ff;
  --border: #1a354d;
  --green: #34d399;
  --yellow: #fbbf24;
  --red: #f87171;
  --blue: #60a5fa;
}

html, body, #root {
  margin: 0;
  min-height: 100%;
  min-width: 100%;
  background: var(--bg);
  color: var(--text);
  font-family: Inter, system-ui, sans-serif;
}

body {
  min-height: 100vh;
}

button, input {
  font: inherit;
}

.app-shell {
  display: grid;
  grid-template-columns: 260px 1fr;
  min-height: 100vh;
}

.sidebar {
  background: var(--panel);
  border-right: 1px solid var(--border);
  padding: 1.25rem;
}

.sidebar h1 {
  margin: 0 0 1.5rem;
  font-size: 1.4rem;
}

.sidebar nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.nav-item {
  background: transparent;
  color: var(--text);
  border: 1px solid var(--border);
  padding: 0.7rem 0.9rem;
  border-radius: 10px;
  text-align: left;
}

.content {
  padding: 1.5rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1rem;
}

.stat-card small {
  display: block;
  color: var(--muted);
  margin-bottom: 0.4rem;
}

.stat-card strong {
  font-size: 1.8rem;
}

.panel {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1rem;
}

.row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.badge {
  display: inline-flex;
  align-items: center;
  padding: 0.3rem 0.6rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
}

.badge.low { background: rgba(52, 211, 153, 0.12); color: var(--green); }
.badge.medium { background: rgba(251, 191, 36, 0.12); color: var(--yellow); }
.badge.high { background: rgba(248, 113, 113, 0.12); color: var(--red); }
.badge.critical { background: rgba(239, 68, 68, 0.18); color: #fca5a5; }

.login-box {
  max-width: 420px;
  margin: 6rem auto;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 2rem;
}

.login-box input {
  width: 100%;
  background: rgba(255,255,255,0.02);
  border: 1px solid var(--border);
  color: var(--text);
  padding: 0.8rem 1rem;
  border-radius: 10px;
  margin-top: 0.5rem;
  margin-bottom: 1rem;
}

.primary-button {
  width: 100%;
  background: linear-gradient(135deg, #1d4ed8, #2563eb);
  color: white;
  border: none;
  border-radius: 10px;
  padding: 0.8rem 1rem;
  cursor: pointer;
  font-weight: 600;
}
