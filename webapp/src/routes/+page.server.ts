import type { Activity, User } from "../types";

const API_BASE: string = "http://192.168.1.17:5055";

export async function load({ url }) {
  const activitiesRes = await fetch(`${API_BASE}/activities`);
  const activities: Activity[] = await activitiesRes.json();

  const userId = url.searchParams.get("user_id");
  const userRes = await fetch(`${API_BASE}/users/${userId}`);
  const user: User = await userRes.json();

  return {
    activities: activities,
    user: user,
  };
}
