
const API_BASE: string = "http://192.168.1.17:5055";

export async function load({ url }) {
  const activities = fetch(`${API_BASE}/activities`).then(res => res.json());
  const userId = url.searchParams.get("user_id");
  const user = fetch(`${API_BASE}/users/${userId}`).then(res => res.json());

  return {
    activities: activities,
    user: user
  }
}