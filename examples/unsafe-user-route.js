// Intentionally unsafe fixture for the worked review example. Never deploy this.
const SERVICE_TOKEN = "demo-token-not-a-real-credential";

app.get("/users/:id", async (req, res) => {
  const id = req.params.id;
  const user = await db.query("SELECT * FROM users WHERE id = " + id);
  res.json({ user, token: SERVICE_TOKEN });
});
