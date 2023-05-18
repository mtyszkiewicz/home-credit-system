
const API_BASE = "http://192.168.1.17:5055"

export async function load({ url }) {
  const activities = fetch(`${API_BASE}/activities`).then(res => res.json())

  let userId = url.searchParams.get("user_id");
  const user = fetch(`${API_BASE}/users/${userId}`).then(res => res.json())

  const summary = fetch(`${API_BASE}/summary`).then(res => res.json())

  return {
    activities: activities,
    user: user,
    summary: summary
  }
}