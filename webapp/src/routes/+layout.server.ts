const API_BASE: string = "http://192.168.1.17:5055";

export async function load({ url }) {
  const userId = url.searchParams.get("user_id");

  if (userId === null) {
    return {}
  }

  const user = fetch(`${API_BASE}/users/${userId}`).then(res => res.json());
  return {
    user: user
  }
}