import { StatusBadge } from '../components/StatusBadge';

const stats = [
  { label: 'Total Alerts', value: 128 },
  { label: 'Critical', value: 9 },
  { label: 'High', value: 21 },
  { label: 'Open Incidents', value: 7 },
];

const DashboardPage = () => {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <h1>AI-SOC</h1>
        <nav>
          <button className="nav-item">Overview</button>
          <button className="nav-item">Alerts</button>
          <button className="nav-item">Incidents</button>
          <button className="nav-item">Threat Intel</button>
          <button className="nav-item">MITRE</button>
          <button className="nav-item">Reports</button>
          <button className="nav-item">Users</button>
        </nav>
      </aside>

      <main className="content">
        <div className="row">
          <h2>Security Operations Overview</h2>
          <StatusBadge level="critical" text="Threat level: Elevated" />
        </div>

        <section className="card-grid">
          {stats.map((stat) => (
            <div key={stat.label} className="stat-card">
              <small>{stat.label}</small>
              <strong>{stat.value}</strong>
            </div>
          ))}
        </section>

        <section className="panel">
          <h3>Recent Alert Summary</h3>
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
              <tr>
                <th style={{ textAlign: 'left', padding: '0.75rem 0' }}>Alert</th>
                <th style={{ textAlign: 'left' }}>Severity</th>
                <th style={{ textAlign: 'left' }}>Source IP</th>
                <th style={{ textAlign: 'left' }}>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Repeated password failures</td>
                <td><StatusBadge level="high" text="HIGH" /></td>
                <td>192.0.2.10</td>
                <td>NEW</td>
              </tr>
              <tr>
                <td>Port scan activity</td>
                <td><StatusBadge level="medium" text="MEDIUM" /></td>
                <td>203.0.113.42</td>
                <td>TRIAGED</td>
              </tr>
            </tbody>
          </table>
        </section>
      </main>
    </div>
  );
};

export default DashboardPage;
