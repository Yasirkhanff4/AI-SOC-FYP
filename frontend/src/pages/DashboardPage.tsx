const LoginPage = () => {
  return (
    <div className="login-box">
      <h2>AI-SOC Login</h2>
      <form>
        <label>
          Username
          <input type="text" defaultValue="admin" />
        </label>
        <label>
          Password
          <input type="password" defaultValue="StrongPass123!" />
        </label>
        <button className="primary-button" type="button">Sign In</button>
      </form>
    </div>
  );
};

export default LoginPage;
